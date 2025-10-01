"""
This module uploads analyzed icon data to Notion database with rate limiting 
so that metadata is stored in searchable format. This is used in upload pipeline.
"""

import logging
import json
import time
from datetime import datetime
from pathlib import Path
from notion_client import Client
from tqdm import tqdm
from src import config


# Configure logging for this module
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def getNotionClient():
    """
    This function uses notion-client SDK to initialize API connection 
    so that database operations are possible. This is used for all Notion calls.
    """
    apiKeys = config.getApiKeys()
    notionToken = apiKeys['notion']
    
    if not notionToken:
        raise ValueError("NOTION_API_TOKEN not configured in .env")
    
    client = Client(auth=notionToken)
    logger.info("Notion client initialized")
    return client


def loadAnalysisData(analysisPath):
    """
    This function uses json.load to read analysis results from disk 
    so that icon metadata is available. This is used at pipeline start.
    """
    if not analysisPath.exists():
        raise FileNotFoundError(f"Analysis file not found: {analysisPath}")
    
    with open(analysisPath, 'r') as analysisFile:
        analysisData = json.load(analysisFile)
    
    logger.info(f"Loaded analysis data for {len(analysisData)} icons")
    return analysisData


def loadUploadCheckpoint(checkpointPath):
    """
    This function uses json.load to read upload progress state 
    so that upload can resume. This is used at pipeline start.
    """
    if not checkpointPath.exists():
        return {'uploaded_icons': []}
    
    try:
        with open(checkpointPath, 'r') as checkpointFile:
            checkpoint = json.load(checkpointFile)
        
        uploadedCount = len(checkpoint.get('uploaded_icons', []))
        logger.info(f"Loaded upload checkpoint: {uploadedCount} icons uploaded")
        return checkpoint
        
    except Exception as error:
        logger.warning(f"Failed to load upload checkpoint: {error}")
        return {'uploaded_icons': []}


def saveUploadCheckpoint(checkpointPath, uploadedIcons, failedIcons):
    """
    This function uses json.dump to save upload progress to disk 
    so that resume is possible. This is used periodically during upload.
    """
    checkpoint = {
        'uploaded_icons': uploadedIcons,
        'failed_icons': failedIcons,
        'timestamp': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    
    with open(checkpointPath, 'w') as checkpointFile:
        json.dump(checkpoint, checkpointFile, indent=2)


def buildNotionPage(iconName, analysisData, iconBaseUrl):
    """
    This function uses Notion page format to structure icon metadata 
    so that page creation has correct schema. This is used per icon upload.
    """
    # Build icon URL
    iconUrl = f"{iconBaseUrl}/{iconName}.png"
    
    # Extract analysis fields with safe defaults
    visualDesc = analysisData.get('visual_description', 'No description available')
    primaryFunc = analysisData.get('primary_function', 'UI Element')
    usageContexts = analysisData.get('usage_contexts', [])
    relatedConcepts = analysisData.get('related_concepts', [])
    colorPalette = analysisData.get('color_palette', 'Monochrome')
    style = analysisData.get('style', 'Line')
    complexity = analysisData.get('complexity', 'Simple')
    
    # Convert related concepts array to text
    relatedConceptsText = ', '.join(relatedConcepts) if relatedConcepts else ''
    
    # Build Notion page properties
    pageProperties = {
        "Name": {
            "title": [{"text": {"content": iconName}}]
        },
        "Icon": {
            "files": [{"name": f"{iconName}.png", "external": {"url": iconUrl}}]
        },
        "Visual Description": {
            "rich_text": [{"text": {"content": visualDesc[:2000]}}]
        },
        "Primary Function": {
            "select": {"name": primaryFunc}
        },
        "Usage Contexts": {
            "multi_select": [{"name": ctx[:100]} for ctx in usageContexts[:10]]
        },
        "Related Concepts": {
            "rich_text": [{"text": {"content": relatedConceptsText[:2000]}}]
        },
        "Color Palette": {
            "select": {"name": colorPalette}
        },
        "Style": {
            "select": {"name": style}
        },
        "Complexity": {
            "select": {"name": complexity}
        },
        "Upload Date": {
            "date": {"start": datetime.utcnow().strftime('%Y-%m-%d')}
        },
        "Processing Status": {
            "select": {"name": "Success"}
        }
    }
    
    return pageProperties


def uploadOnePage(client, databaseId, pageProperties, maxRetries=3):
    """
    This function uses Notion API to create single page with retries 
    so that icon data is uploaded. This is used per icon.
    """
    sleeper = config.makeBackoffSleeper(maxRetries)
    
    for attempt in range(maxRetries):
        try:
            response = client.pages.create(
                parent={"database_id": databaseId},
                properties=pageProperties
            )
            
            return True, None
            
        except Exception as error:
            errorMsg = f"Upload failed: {str(error)}"
            logger.warning(f"Attempt {attempt + 1}/{maxRetries}: {errorMsg}")
            
            if attempt < maxRetries - 1:
                sleeper(attempt)
                continue
            else:
                return False, errorMsg
    
    return False, "Max retries exceeded"


def respectRateLimit():
    """
    This function uses time.sleep to enforce delay between requests 
    so that Notion rate limits are respected. This is used after each upload.
    """
    rateLimits = config.getRateLimits()
    notionRps = rateLimits['notionRps']
    
    # Calculate delay to respect RPS limit
    delaySecs = 1.0 / notionRps
    
    time.sleep(delaySecs)


def run():
    """
    This function uses Notion API to upload all analyzed icons to database 
    so that data is searchable in Notion. This is the main entry point.
    """
    logger.info("Starting Notion upload pipeline")
    
    # Get configuration
    paths = config.getPaths()
    databaseId = config.getNotionDatabaseId()
    iconBaseUrl = config.getIconBaseUrl()
    checkpointInterval = config.getCheckpointInterval()
    
    if not databaseId or databaseId.strip() == '':
        raise ValueError("NOTION_DATABASE_ID not set. Run create_notion_db.py first")
    
    # Initialize Notion client
    client = getNotionClient()
    
    # Load analysis data
    analysisData = loadAnalysisData(paths['analysisJson'])
    
    if len(analysisData) == 0:
        logger.warning("No analysis data found to upload")
        return
    
    # Load upload checkpoint
    uploadCheckpoint = loadUploadCheckpoint(paths['checkpointJson'])
    uploadedIcons = set(uploadCheckpoint.get('uploaded_icons', []))
    failedIcons = uploadCheckpoint.get('failed_icons', [])
    
    # Get icons to upload (excluding already uploaded)
    iconsToUpload = [name for name in analysisData.keys() if name not in uploadedIcons]
    
    logger.info(f"Found {len(iconsToUpload)} icons to upload")
    
    # Track statistics
    successCount = 0
    failedCount = 0
    
    # Upload each icon with progress bar
    for idx, iconName in enumerate(tqdm(iconsToUpload, desc="Uploading to Notion")):
        analysis = analysisData[iconName]
        
        # Build page properties
        pageProps = buildNotionPage(iconName, analysis, iconBaseUrl)
        
        # Upload page
        success, errorMsg = uploadOnePage(client, databaseId, pageProps)
        
        if success:
            uploadedIcons.add(iconName)
            successCount += 1
        else:
            failedIcons.append({'icon': iconName, 'error': errorMsg})
            failedCount += 1
            
            # Log failure
            with open(paths['failedLog'], 'a') as logFile:
                logFile.write(f"Upload failed: {iconName} - {errorMsg}\n")
        
        # Save checkpoint periodically
        if (idx + 1) % checkpointInterval == 0:
            saveUploadCheckpoint(
                paths['checkpointJson'],
                list(uploadedIcons),
                failedIcons
            )
            logger.info(f"Checkpoint saved at {idx + 1} uploads")
        
        # Respect rate limit
        respectRateLimit()
    
    # Save final checkpoint
    saveUploadCheckpoint(
        paths['checkpointJson'],
        list(uploadedIcons),
        failedIcons
    )
    
    # Report statistics
    logger.info("Upload complete:")
    logger.info(f"  Successful: {successCount}")
    logger.info(f"  Failed: {failedCount}")
    logger.info(f"  Total uploaded: {len(uploadedIcons)}")
    
    if failedCount > 0:
        logger.warning(f"Check {paths['failedLog']} for failure details")


if __name__ == '__main__':
    run()
