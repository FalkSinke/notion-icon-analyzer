"""
This module loads configuration from .env file and provides helper functions 
so that other modules can access settings. This is used throughout the system.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import time


def loadEnv():
    """
    This function uses dotenv to load environment variables from .env file 
    so that configuration is available. This is used at module startup.
    """
    # Get the project root directory (parent of src/)
    projectRoot = Path(__file__).parent.parent
    envPath = projectRoot / '.env'
    load_dotenv(envPath)


def validateEnv():
    """
    This function uses os.getenv to check required variables exist 
    so that missing configuration is detected early. This is used before operations.
    """
    requiredVars = [
        'GOOGLE_API_KEY',
        'NOTION_API_TOKEN', 
        'ICON_BASE_URL'
    ]
    
    missingVars = []
    for varName in requiredVars:
        value = os.getenv(varName)
        if not value or value.strip() == '':
            missingVars.append(varName)
    
    if missingVars:
        errorMsg = f"Missing required environment variables: {', '.join(missingVars)}"
        raise ValueError(errorMsg)


def getPaths():
    """
    This function uses os.getenv to retrieve directory paths from config 
    so that file locations are centralized. This is used in file operations.
    """
    projectRoot = Path(__file__).parent.parent
    
    # Get paths from env or use defaults relative to project root
    iconInputDir = os.getenv('ICON_INPUT_DIR', 'notion_icons')
    pngOutputDir = os.getenv('PNG_OUTPUT_DIR', 'png_icons')
    outputDir = os.getenv('OUTPUT_DIR', 'output')
    
    paths = {
        'iconInput': projectRoot / iconInputDir,
        'pngOutput': projectRoot / pngOutputDir,
        'output': projectRoot / outputDir,
        'analysisJson': projectRoot / outputDir / 'icon_analysis.json',
        'checkpointJson': projectRoot / outputDir / 'checkpoint.json',
        'failedLog': projectRoot / outputDir / 'failed_icons.log'
    }
    
    return paths


def ensureDirs():
    """
    This function uses Path.mkdir to create output directories if missing 
    so that file operations don't fail. This is used during initialization.
    """
    paths = getPaths()
    
    # Create directories that should exist
    paths['pngOutput'].mkdir(exist_ok=True, parents=True)
    paths['output'].mkdir(exist_ok=True, parents=True)


def getApiKeys():
    """
    This function uses os.getenv to retrieve API credentials from config 
    so that authentication is handled securely. This is used in API clients.
    """
    apiKeys = {
        'google': os.getenv('GOOGLE_API_KEY'),
        'notion': os.getenv('NOTION_API_TOKEN')
    }
    
    return apiKeys


def getRateLimits():
    """
    This function uses os.getenv to get rate limit settings with defaults 
    so that API calls respect limits. This is used in API request loops.
    """
    rateLimits = {
        'geminiRpm': int(os.getenv('GEMINI_RPM', '60')),
        'notionRps': int(os.getenv('NOTION_RPS', '2'))
    }
    
    return rateLimits


def getCheckpointInterval():
    """
    This function uses os.getenv to get checkpoint save frequency 
    so that progress is saved regularly. This is used in batch processing.
    """
    return int(os.getenv('CHECKPOINT_INTERVAL', '50'))


def getGeminiModelName():
    """
    This function uses os.getenv to get the Gemini model identifier 
    so that the correct AI model is used. This is used in analysis setup.
    """
    return os.getenv('GEMINI_MODEL', 'gemini-2.0-flash-exp')


def getNotionParentPageId():
    """
    This function uses os.getenv to get parent page ID for database creation 
    so that database is created in correct location. This is used in DB setup.
    """
    return os.getenv('NOTION_PARENT_PAGE_ID')


def getNotionDatabaseId():
    """
    This function uses os.getenv to get existing database ID 
    so that uploads target the correct database. This is used in upload operations.
    """
    return os.getenv('NOTION_DATABASE_ID')


def getIconBaseUrl():
    """
    This function uses os.getenv to get base URL for serving PNG files 
    so that Notion can access icon images. This is used in upload operations.
    """
    iconBaseUrl = os.getenv('ICON_BASE_URL')
    
    if not iconBaseUrl or iconBaseUrl.strip() == '':
        raise ValueError("ICON_BASE_URL must be set to an externally accessible HTTPS URL")
    
    # Ensure URL ends without trailing slash for consistent path joining
    return iconBaseUrl.rstrip('/')


def makeBackoffSleeper(maxRetries=3):
    """
    This function uses closure to create exponential backoff sleep calculator 
    so that failed requests are retried with increasing delays. This is used in error handling.
    """
    def sleepForRetry(attemptNumber):
        """
        This function uses exponential formula to calculate retry delay 
        so that API rate limits are respected. This is used after request failures.
        """
        if attemptNumber >= maxRetries:
            return None
        
        # Exponential backoff: 2^attempt seconds (1s, 2s, 4s)
        delaySecs = 2 ** attemptNumber
        time.sleep(delaySecs)
        return delaySecs
    
    return sleepForRetry


# Initialize environment on module import
loadEnv()
