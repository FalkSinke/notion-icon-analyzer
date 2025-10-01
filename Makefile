# Makefile for Icon Analysis & Notion Upload Pipeline
# This file provides convenient CLI commands for running pipeline stages

.PHONY: help install convert create-db analyze upload all clean test

# Default target shows help
help:
	@echo "Icon Analysis & Notion Upload Pipeline"
	@echo ""
	@echo "Available commands:"
	@echo "  make install      - Install dependencies in virtual environment"
	@echo "  make convert      - Convert SVG icons to PNG format"
	@echo "  make create-db    - Create Notion database with schema"
	@echo "  make analyze      - Analyze icons with Gemini AI"
	@echo "  make upload       - Upload analyzed data to Notion"
	@echo "  make all          - Run complete pipeline (convert -> analyze -> upload)"
	@echo "  make test         - Run test suite"
	@echo "  make clean        - Remove generated files (PNGs, output, checkpoints)"
	@echo "  make clean-all    - Remove all generated files and virtual environment"

# Install dependencies
install:
	@echo "Installing dependencies..."
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	@echo "Installation complete. Activate with: source venv/bin/activate"

# Convert SVG to PNG
convert:
	@echo "Converting SVG icons to PNG..."
	python -m src.convert_svg_to_png

# Create Notion database
create-db:
	@echo "Creating Notion database..."
	python -m src.create_notion_db

# Analyze icons with Gemini
analyze:
	@echo "Analyzing icons with Gemini AI..."
	python -m src.analyze_icons

# Upload to Notion
upload:
	@echo "Uploading to Notion database..."
	python -m src.upload_to_notion

# Run complete pipeline
all: convert analyze upload
	@echo "Pipeline complete!"

# Run tests
test:
	@echo "Running test suite..."
	pytest tests/ -v

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -rf png_icons/*
	rm -rf output/*
	@echo "Clean complete. Source SVGs preserved."

# Clean everything including venv
clean-all: clean
	@echo "Removing virtual environment..."
	rm -rf venv/
	@echo "Full clean complete."
