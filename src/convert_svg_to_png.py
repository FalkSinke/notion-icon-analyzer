"""
This module converts SVG icons to PNG format using cairosvg library 
so that images are compatible with Gemini API. This is used as first pipeline step.
"""

import logging
from pathlib import Path
import cairosvg
from tqdm import tqdm
from src import config


# Configure logging for this module
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def listSvgFiles(inputDir):
    """
    This function uses Path.glob to find all SVG files in directory 
    so that conversion targets are identified. This is used at pipeline start.
    """
    svgPath = Path(inputDir)
    
    if not svgPath.exists():
        raise FileNotFoundError(f"Icon directory not found: {inputDir}")
    
    # Get all .svg files, sorted alphabetically for consistent ordering
    svgFiles = sorted(svgPath.glob('*.svg'))
    
    logger.info(f"Found {len(svgFiles)} SVG files in {inputDir}")
    return svgFiles


def ensureOutputDirs(outputDir):
    """
    This function uses Path.mkdir to create PNG output directory 
    so that converted files have destination. This is used before conversion.
    """
    outputPath = Path(outputDir)
    outputPath.mkdir(exist_ok=True, parents=True)
    logger.info(f"Output directory ready: {outputDir}")


def convertOneSvg(svgFilePath, outputDir, targetSize=512):
    """
    This function uses cairosvg to convert single SVG to PNG format 
    so that icon is readable by vision API. This is used per file.
    """
    svgPath = Path(svgFilePath)
    outputPath = Path(outputDir)
    
    # Create output filename with same name but .png extension
    pngFileName = svgPath.stem + '.png'
    pngFilePath = outputPath / pngFileName
    
    try:
        # Convert SVG to PNG with specified dimensions
        cairosvg.svg2png(
            url=str(svgPath),
            write_to=str(pngFilePath),
            output_width=targetSize,
            output_height=targetSize
        )
        return True, None
        
    except Exception as error:
        errorMsg = f"Conversion failed for {svgPath.name}: {str(error)}"
        return False, errorMsg


def shouldSkip(pngFilePath):
    """
    This function uses Path.exists to check if PNG already created 
    so that redundant conversions are avoided. This is used for resume capability.
    """
    pngPath = Path(pngFilePath)
    
    # Skip if file exists and has non-zero size
    if pngPath.exists() and pngPath.stat().st_size > 0:
        return True
    
    return False


def logFailure(failureMessage, failedLogPath):
    """
    This function uses file append to record conversion failures 
    so that errors are tracked for review. This is used when conversion fails.
    """
    logPath = Path(failedLogPath)
    
    with open(logPath, 'a') as logFile:
        logFile.write(f"{failureMessage}\n")


def run():
    """
    This function uses config and cairosvg to convert all SVG files 
    so that PNG versions are ready for analysis. This is the main entry point.
    """
    logger.info("Starting SVG to PNG conversion pipeline")
    
    # Get configuration
    paths = config.getPaths()
    config.ensureDirs()
    
    # Find all SVG files
    svgFiles = listSvgFiles(paths['iconInput'])
    
    if len(svgFiles) == 0:
        logger.warning("No SVG files found to convert")
        return
    
    # Track statistics
    convertedCount = 0
    skippedCount = 0
    failedCount = 0
    
    # Process each SVG file with progress bar
    for svgFile in tqdm(svgFiles, desc="Converting SVGs"):
        # Generate output path
        pngFileName = svgFile.stem + '.png'
        pngFilePath = paths['pngOutput'] / pngFileName
        
        # Skip if already exists
        if shouldSkip(pngFilePath):
            skippedCount += 1
            continue
        
        # Attempt conversion
        success, errorMsg = convertOneSvg(
            svgFile,
            paths['pngOutput']
        )
        
        if success:
            convertedCount += 1
        else:
            failedCount += 1
            logFailure(errorMsg, paths['failedLog'])
            logger.error(errorMsg)
    
    # Report final statistics
    logger.info(f"Conversion complete:")
    logger.info(f"  Converted: {convertedCount}")
    logger.info(f"  Skipped (already exist): {skippedCount}")
    logger.info(f"  Failed: {failedCount}")
    
    if failedCount > 0:
        logger.warning(f"Check {paths['failedLog']} for failure details")


if __name__ == '__main__':
    run()
