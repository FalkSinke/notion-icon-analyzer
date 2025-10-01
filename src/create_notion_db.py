"""
This module creates Notion database with predefined schema for icon metadata 
so that analysis results have structured storage. This is used for database setup.
"""

import logging
from notion_client import Client
from pathlib import Path
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


def buildDatabaseSchema():
    """
    This function uses Notion schema format to define database properties 
    so that icon metadata is structured correctly. This is used in database creation.
    """
    schema = {
        "Name": {"title": {}},
        
        "Icon": {"files": {}},
        
        "Visual Description": {"rich_text": {}},
        
        "Primary Function": {
            "select": {
                "options": [
                    {"name": "UI Element", "color": "blue"},
                    {"name": "Action", "color": "green"},
                    {"name": "Object", "color": "yellow"},
                    {"name": "Concept", "color": "purple"}
                ]
            }
        },
        
        "Usage Contexts": {"multi_select": {"options": []}},
        
        "Related Concepts": {"rich_text": {}},
        
        "Color Palette": {
            "select": {
                "options": [
                    {"name": "Monochrome", "color": "gray"},
                    {"name": "Blue", "color": "blue"},
                    {"name": "Green", "color": "green"},
                    {"name": "Red", "color": "red"},
                    {"name": "Yellow", "color": "yellow"},
                    {"name": "Purple", "color": "purple"},
                    {"name": "Multicolor", "color": "pink"}
                ]
            }
        },
        
        "Style": {
            "select": {
                "options": [
                    {"name": "Line", "color": "gray"},
                    {"name": "Filled", "color": "blue"},
                    {"name": "Outline", "color": "green"},
                    {"name": "Gradient", "color": "purple"}
                ]
            }
        },
        
        "Complexity": {
            "select": {
                "options": [
                    {"name": "Simple", "color": "green"},
                    {"name": "Medium", "color": "yellow"},
                    {"name": "Detailed", "color": "red"}
                ]
            }
        },
        
        "Upload Date": {"date": {}},
        
        "Processing Status": {
            "select": {
                "options": [
                    {"name": "Success", "color": "green"},
                    {"name": "Failed", "color": "red"},
                    {"name": "Pending", "color": "gray"}
                ]
            }
        }
    }
    
    logger.info("Database schema built with 11 properties")
    return schema


def createDatabase(client, parentPageId, databaseTitle="Icon Analysis"):
    """
    This function uses Notion API to create new database with schema 
    so that icon data has destination. This is used once per setup.
    """
    if not parentPageId:
        raise ValueError("NOTION_PARENT_PAGE_ID not configured in .env")
    
    schema = buildDatabaseSchema()
    
    try:
        response = client.databases.create(
            parent={"page_id": parentPageId},
            title=[{"type": "text", "text": {"content": databaseTitle}}],
            properties=schema
        )
        
        databaseId = response['id']
        databaseUrl = response['url']
        
        logger.info(f"Database created successfully")
        logger.info(f"Database ID: {databaseId}")
        logger.info(f"Database URL: {databaseUrl}")
        
        return databaseId, databaseUrl
        
    except Exception as error:
        errorMsg = f"Failed to create database: {str(error)}"
        logger.error(errorMsg)
        raise


def writeDatabaseIdToEnv(databaseId):
    """
    This function uses file operations to update .env with database ID 
    so that upload script knows target. This is used after database creation.
    """
    projectRoot = Path(__file__).parent.parent
    envPath = projectRoot / '.env'
    
    # Read existing .env content
    with open(envPath, 'r') as envFile:
        lines = envFile.readlines()
    
    # Update NOTION_DATABASE_ID line
    updated = False
    for idx, line in enumerate(lines):
        if line.startswith('NOTION_DATABASE_ID='):
            lines[idx] = f'NOTION_DATABASE_ID={databaseId}\n'
            updated = True
            break
    
    # Write back to file
    with open(envPath, 'w') as envFile:
        envFile.writelines(lines)
    
    if updated:
        logger.info(f"Updated .env with NOTION_DATABASE_ID={databaseId}")
    else:
        logger.warning("NOTION_DATABASE_ID line not found in .env")


def run():
    """
    This function uses Notion API and config to create database with schema 
    so that icon analysis pipeline has destination. This is the main entry point.
    """
    logger.info("Starting Notion database creation")
    
    # Check if database already exists
    existingDbId = config.getNotionDatabaseId()
    if existingDbId and existingDbId.strip():
        logger.warning(f"Database already exists: {existingDbId}")
        userInput = input("Create new database anyway? (y/n): ")
        if userInput.lower() != 'y':
            logger.info("Database creation cancelled")
            return
    
    # Get configuration
    parentPageId = config.getNotionParentPageId()
    
    # Initialize Notion client
    client = getNotionClient()
    
    # Create database
    databaseId, databaseUrl = createDatabase(client, parentPageId)
    
    # Save database ID to .env
    writeDatabaseIdToEnv(databaseId)
    
    logger.info("Database setup complete")
    logger.info(f"View database at: {databaseUrl}")


if __name__ == '__main__':
    run()
