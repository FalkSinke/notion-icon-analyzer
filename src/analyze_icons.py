"""
This module analyzes PNG icons using Gemini vision API to extract metadata 
so that icons have semantic descriptions. This is used in analysis pipeline.
"""

import logging
import json
import time
from pathlib import Path
from PIL import Image
import google.generativeai as genai
from tqdm import tqdm
from src import config


# Configure logging for this module
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def initializeGemini():
    """
    This function uses google.generativeai to configure API client 
    so that vision analysis is possible. This is used at pipeline start.
    """
    apiKeys = config.getApiKeys()
    googleKey = apiKeys['google']
    
    if not googleKey:
        raise ValueError("GOOGLE_API_KEY not configured in .env")
    
    genai.configure(api_key=googleKey)
    modelName = config.getGeminiModelName()
    model = genai.GenerativeModel(modelName)
    
    logger.info(f"Gemini API initialized with model: {modelName}")
    return model


def buildAnalysisPrompt():
    """
    This function uses structured format to create Gemini prompt template 
    so that analysis output is consistent JSON. This is used per icon analysis.
    """
    prompt = """You are an expert iconography analyst. Return ONLY valid JSON.

{
  "visual_description": "Detailed description in 2-3 sentences",
  "primary_function": "Category: UI Element, Action, Object, or Concept",
  "usage_contexts": ["context1", "context2", "context3", "context4", "context5"],
  "related_concepts": ["concept1", "concept2", "concept3", "concept4", "concept5", "concept6", "concept7", "concept8", "concept9", "concept10"],
  "color_palette": "Color: Monochrome, Blue, Green, Red, Yellow, Purple, Multicolor",
  "style": "Style: Line, Filled, Outline, or Gradient",
  "complexity": "Level: Simple, Medium, or Detailed"
}

Return 5-7 usage_contexts and 10-15 related_concepts for semantic search."""
    
    return prompt


def listPngFiles(pngDir):
    """
    This function uses Path.glob to find all PNG files in directory 
    so that analysis targets are identified. This is used at pipeline start.
    """
    pngPath = Path(pngDir)
    
    if not pngPath.exists():
        raise FileNotFoundError(f"PNG directory not found: {pngDir}")
    
    pngFiles = sorted(pngPath.glob('*.png'))
    logger.info(f"Found {len(pngFiles)} PNG files for analysis")
    return pngFiles


def loadCheckpoint(checkpointPath):
    """
    This function uses json.load to read previous progress state 
    so that analysis can resume. This is used at pipeline start.
    """
    if not checkpointPath.exists():
        return {}
    
    try:
        with open(checkpointPath, 'r') as checkpointFile:
            checkpoint = json.load(checkpointFile)
        
        processed = checkpoint.get('last_processed_index', 0)
        logger.info(f"Loaded checkpoint: {processed} icons processed")
        return checkpoint
        
    except Exception as error:
        logger.warning(f"Failed to load checkpoint: {error}")
        return {}


def saveCheckpoint(checkpointPath, lastIndex, failedIcons):
    """
    This function uses json.dump to save progress state to disk 
    so that resume is possible. This is used periodically during analysis.
    """
    checkpoint = {
        'last_processed_index': lastIndex,
        'failed_icons': failedIcons,
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    }
    
    with open(checkpointPath, 'w') as checkpointFile:
        json.dump(checkpoint, checkpointFile, indent=2)


def loadExistingAnalysis(analysisPath):
    """
    This function uses json.load to read previous analysis results 
    so that completed work is preserved. This is used at pipeline start.
    """
    if not analysisPath.exists():
        return {}
    
    try:
        with open(analysisPath, 'r') as analysisFile:
            analysis = json.load(analysisFile)
        
        logger.info(f"Loaded existing analysis with {len(analysis)} icons")
        return analysis
        
    except Exception as error:
        logger.warning(f"Failed to load existing analysis: {error}")
        return {}


def saveAnalysis(analysisPath, analysisData):
    """
    This function uses json.dump to write analysis results to disk 
    so that results are persisted. This is used periodically during analysis.
    """
    with open(analysisPath, 'w') as analysisFile:
        json.dump(analysisData, analysisFile, indent=2)


def parseResponse(responseText):
    """
    This function uses string operations to clean Gemini response text 
    so that JSON can be parsed. This is used after API response.
    """
    # Remove markdown code blocks if present
    if responseText.startswith('```json'):
        responseText = responseText[7:]
    if responseText.startswith('```'):
        responseText = responseText[3:]
    if responseText.endswith('```'):
        responseText = responseText[:-3]
    
    return responseText.strip()


def analyzeOneIcon(model, pngPath, prompt, maxRetries=3):
    """
    This function uses Gemini API to analyze single icon with retries 
    so that metadata is extracted. This is used per icon.
    """
    sleeper = config.makeBackoffSleeper(maxRetries)
    
    for attempt in range(maxRetries):
        try:
            # Load image and send to Gemini
            image = Image.open(pngPath)
            response = model.generate_content([prompt, image])
            
            # Parse JSON response
            responseText = parseResponse(response.text)
            analysisData = json.loads(responseText)
            
            return True, analysisData, None
            
        except json.JSONDecodeError as error:
            errorMsg = f"JSON parse error: {str(error)}"
            logger.warning(f"Attempt {attempt + 1}: {pngPath.name} - {errorMsg}")
            
            if attempt < maxRetries - 1:
                sleeper(attempt)
            else:
                return False, None, errorMsg
                
        except Exception as error:
            errorMsg = f"Analysis failed: {str(error)}"
            logger.warning(f"Attempt {attempt + 1}: {pngPath.name} - {errorMsg}")
            
            if attempt < maxRetries - 1:
                sleeper(attempt)
            else:
                return False, None, errorMsg
    
    return False, None, "Max retries exceeded"


def respectRateLimit():
    """
    This function uses time.sleep to enforce minimum delay between requests 
    so that API rate limits are respected. This is used after each API call.
    """
    rateLimits = config.getRateLimits()
    geminiRpm = rateLimits['geminiRpm']
    
    # Calculate minimum delay with buffer
    minDelaySecs = 60.0 / geminiRpm
    delaySecs = minDelaySecs + 0.1
    
    time.sleep(delaySecs)


def run():
    """
    This function uses Gemini API to analyze all PNG icons with checkpointing 
    so that semantic metadata is generated. This is the main entry point.
    """
    logger.info("Starting icon analysis pipeline")
    
    # Get configuration
    paths = config.getPaths()
    checkpointInterval = config.getCheckpointInterval()
    
    # Initialize Gemini
    model = initializeGemini()
    prompt = buildAnalysisPrompt()
    
    # Find all PNG files
    pngFiles = listPngFiles(paths['pngOutput'])
    
    if len(pngFiles) == 0:
        logger.warning("No PNG files found to analyze")
        return
    
    # Load checkpoint and existing analysis
    checkpoint = loadCheckpoint(paths['checkpointJson'])
    analysisData = loadExistingAnalysis(paths['analysisJson'])
    
    startIndex = checkpoint.get('last_processed_index', 0)
    failedIcons = checkpoint.get('failed_icons', [])
    
    # Process icons with progress bar
    processedCount = 0
    successCount = 0
    failedCount = 0
    
    for idx in tqdm(range(startIndex, len(pngFiles)), desc="Analyzing icons"):
        pngFile = pngFiles[idx]
        iconName = pngFile.stem
        
        # Skip if already analyzed
        if iconName in analysisData:
            processedCount += 1
            successCount += 1
            continue
        
        # Analyze icon
        success, analysis, errorMsg = analyzeOneIcon(model, pngFile, prompt)
        
        if success:
            analysisData[iconName] = analysis
            successCount += 1
        else:
            failedIcons.append(iconName)
            failedCount += 1
            
            with open(paths['failedLog'], 'a') as logFile:
                logFile.write(f"Analysis failed: {iconName} - {errorMsg}\n")
        
        processedCount += 1
        
        # Save checkpoint periodically
        if processedCount % checkpointInterval == 0:
            saveCheckpoint(paths['checkpointJson'], idx + 1, failedIcons)
            saveAnalysis(paths['analysisJson'], analysisData)
            logger.info(f"Checkpoint saved at {processedCount} icons")
        
        # Respect rate limit
        respectRateLimit()
    
    # Save final results
    saveCheckpoint(paths['checkpointJson'], len(pngFiles), failedIcons)
    saveAnalysis(paths['analysisJson'], analysisData)
    
    # Report statistics
    logger.info("Analysis complete:")
    logger.info(f"  Processed: {processedCount}")
    logger.info(f"  Successful: {successCount}")
    logger.info(f"  Failed: {failedCount}")
    
    if failedCount > 0:
        logger.warning(f"Check {paths['failedLog']} for failure details")


if __name__ == '__main__':
    run()
