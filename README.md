# Icon Analysis & Notion Upload System

Automated pipeline for analyzing 884 Notion icons using Gemini 2.5 Flash and uploading them to a Notion database with rich semantic metadata.

**Repository**: [https://github.com/FalkSinke/notion-icon-analyzer](https://github.com/FalkSinke/notion-icon-analyzer)

## Overview

This system processes SVG icons through a three-stage pipeline:
1. **Conversion**: SVG → PNG format for API compatibility
2. **Analysis**: Vision AI extracts visual and semantic metadata
3. **Upload**: Rate-limited batch upload to Notion database

**Total Icons**: 884 SVG files
**Expected Runtime**: 7-8 hours
**Rate Limit**: 2 requests/second to Notion API

---

## Quick Start

### Using Make (Recommended)

```bash
# View all available commands
make help

# Run complete pipeline
make all

# Or run stages individually
make convert      # Convert SVGs to PNGs
make create-db    # Create Notion database
make analyze      # Analyze with Gemini
make upload       # Upload to Notion
```

### Manual Execution

```bash
# Activate virtual environment
source venv/bin/activate

# Run stages
python -m src.convert_svg_to_png
python -m src.create_notion_db
python -m src.analyze_icons
python -m src.upload_to_notion
```

---

## Architecture

### Components

```
iconupload/
├── notion_icons/           # Source SVG files (884 icons)
├── png_icons/              # Converted PNG files (generated)
├── output/                 # Analysis results and logs
│   ├── icon_analysis.json
│   ├── checkpoint.json
│   └── failed_icons.log
├── src/                    # Source code
│   ├── config.py           # Configuration management (175 lines)
│   ├── convert_svg_to_png.py  # SVG converter (158 lines)
│   ├── create_notion_db.py    # Database creator (210 lines)
│   ├── analyze_icons.py       # Gemini analyzer (299 lines)
│   └── upload_to_notion.py    # Notion uploader (285 lines)
├── tests/                  # Test suite
├── venv/                   # Virtual environment
├── Makefile                # CLI automation
├── requirements.txt
├── .env                    # API keys (not committed)
└── README.md
```

### Module Overview

**config.py** (175 lines):
- Environment variable loading and validation
- Path management and directory creation
- API key retrieval
- Rate limit configuration
- Exponential backoff helper

**convert_svg_to_png.py** (158 lines):
- SVG file discovery
- CairoSVG conversion (512x512 PNG)
- Resume capability (skips existing)
- Failure logging

**create_notion_db.py** (210 lines):
- Notion API client initialization
- Database schema definition (11 properties)
- Database creation and ID persistence
- .env file update

**analyze_icons.py** (299 lines):
- Gemini 2.0 Flash initialization
- Structured JSON prompt
- Batch processing with checkpoints
- Rate limiting (60 RPM)
- Exponential backoff retry logic

**upload_to_notion.py** (285 lines):
- Notion page builder
- Rate-limited upload (2 RPS)
- Resume from checkpoint
- Icon URL generation

---

## Notion Database Schema

| Property | Type | Description |
|----------|------|-------------|
| **Name** | Title | Filename without extension |
| **Icon** | Files & Media | The PNG file |
| **Visual Description** | Rich Text | Detailed appearance description |
| **Primary Function** | Select | Main category (UI, Action, Object, Concept) |
| **Usage Contexts** | Multi-select | 5-7 specific use cases |
| **Related Concepts** | Rich Text | 10-15 semantically related terms |
| **Color Palette** | Select | Dominant color scheme |
| **Style** | Select | Design style (Line, Filled, Outline, Gradient) |
| **Complexity** | Select | Simple, Medium, Detailed |
| **Upload Date** | Date | Timestamp |
| **Processing Status** | Select | Success, Failed, Pending |

---

## Gemini Analysis Prompt

```json
{
  "visual_description": "Detailed description of shapes, composition, visual elements",
  "primary_function": "Single category classification",
  "usage_contexts": ["context1", "context2", ...],
  "related_concepts": ["concept1", "concept2", ...],
  "color_palette": "dominant color description",
  "style": "design style classification",
  "complexity": "simple|medium|detailed"
}
```

**Related Concepts Focus**:
- Direct synonyms and broader categories
- Related actions or states
- Industry-specific applications
- Abstract concepts and metaphorical uses
- Terms enabling semantic LLM search

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/FalkSinke/notion-icon-analyzer.git
cd notion-icon-analyzer
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Edit `.env` file:

```env
# Gemini API Configuration
GOOGLE_API_KEY=your_gemini_api_key_here

# Notion API Configuration
NOTION_API_TOKEN=your_notion_integration_token_here
NOTION_PARENT_PAGE_ID=your_parent_page_id_here
NOTION_DATABASE_ID=will_be_generated

# Directory Paths (relative to project root)
ICON_INPUT_DIR=notion_icons
PNG_OUTPUT_DIR=png_icons
OUTPUT_DIR=output

# Model Configuration
GEMINI_MODEL=gemini-2.0-flash-exp

# Rate Limits
GEMINI_RPM=60
NOTION_RPS=2

# Processing Configuration
CHECKPOINT_INTERVAL=50

# Icon Base URL for Notion (externally accessible HTTPS URL)
ICON_BASE_URL=https://your-hosting-url.com/icons
```

---

## Usage

### Step 1: Convert SVG to PNG

```bash
make convert
# or
python -m src.convert_svg_to_png
```

- Converts all 884 SVG files to PNG format
- Output: `png_icons/` directory
- Progress: Real-time with tqdm
- Resume: Skips existing files

### Step 2: Create Notion Database

```bash
make create-db
# or
python -m src.create_notion_db
```

- Creates database with predefined schema
- Updates `.env` with `NOTION_DATABASE_ID`
- Returns: Database URL

### Step 3: Analyze Icons with Gemini

```bash
make analyze
# or
python -m src.analyze_icons
```

- Batch processes icons through Gemini 2.0 Flash
- Output: `output/icon_analysis.json`
- Checkpoint: Saves progress every 50 icons
- Resume: Automatically continues from last checkpoint

### Step 4: Upload to Notion

```bash
make upload
# or
python -m src.upload_to_notion
```

- Rate-limited upload (2 requests/second)
- Progress tracking with success/failure counts
- Resume: Continues from last uploaded icon
- Output: `output/failed_icons.log` for manual review

### Resume After Interruption

All scripts support automatic resume from checkpoint:

```bash
# Analysis resumes from last processed icon
make analyze

# Upload resumes from last uploaded icon
make upload
```

---

## Error Handling

### Retry Logic

- Exponential backoff for API failures
- Maximum 3 retries per request
- Failed items logged to `output/failed_icons.log`

### Checkpoint System

```json
{
  "last_processed_index": 450,
  "failed_icons": ["icon-name-1", "icon-name-2"],
  "timestamp": "2025-09-30T19:58:30Z"
}
```

### Resume Capability

- Automatically detects existing checkpoint
- Skips already processed icons
- Regenerates analysis only for failed items

---

## Testing

Run test suite:

```bash
make test
# or
pytest tests/ -v
```

---

## Progress Log

### Phase 1: Setup & Implementation ✅

- [x] Project structure created
- [x] Virtual environment initialized
- [x] Dependencies installed
- [x] Configuration files created
- [x] GitHub repository created and linked
- [x] **Core modules implemented** (config, converter, analyzer, uploader)
- [x] **Makefile created for CLI automation**
- [x] **All modules under 300 lines**
- [x] **Code style compliance verified**

### Phase 2: Execution (Pending API Configuration)

- [ ] API keys configured in .env
- [ ] ICON_BASE_URL hosting set up
- [ ] SVG to PNG conversion completed (0/884)
- [ ] Notion database created
- [ ] Icons analyzed (0/884)
- [ ] Icons uploaded (0/884)

### Phase 3: Verification (Pending Execution)

- [ ] Upload count verified
- [ ] Database quality checked
- [ ] Failed icons reviewed
- [ ] Final report generated

---

## Technical Details

### Rate Limiting

- **Notion API**: 0.5 seconds between requests (2/second limit)
- **Gemini API**: 1.0+ seconds between requests (60 RPM limit)
- **Exponential Backoff**: 2^attempt seconds (1s, 2s, 4s)

### Memory Management

- Icons processed sequentially
- Incremental JSON saves every 50 items
- Checkpoints prevent data loss

### File Naming Convention

- Input: `icon-arrow-up.svg`
- PNG: `icon-arrow-up.png`
- Analysis key: `icon-arrow-up`

---

## Cost Estimate

- **Gemini 2.0 Flash**: Free tier sufficient (60 RPM)
- **Notion API**: Free tier sufficient (rate limits only)
- **Total Cost**: $0.00

---

## Troubleshooting

### Issue: SVG Conversion Fails

```bash
# Check cairosvg installation
pip install --upgrade cairosvg pillow

# Install Cairo system dependencies (macOS)
brew install cairo pango gdk-pixbuf libffi
```

### Issue: Gemini API Rate Limit

```bash
# Script will automatically retry with backoff
# Adjust GEMINI_RPM in .env if needed
```

### Issue: Notion Upload Timeout

```bash
# Check internet connection
# Verify Notion integration has database access
# Review output/failed_icons.log for specific errors
```

### Issue: Missing Environment Variables

```bash
# Script will report missing variables on startup
# Check .env file for required values
# See .env.example for template
```

---

## Dependencies

- `google-generativeai>=0.3.0` - Gemini API client
- `notion-client>=2.0.0` - Official Notion SDK
- `Pillow>=10.0.0` - Image processing
- `cairosvg>=2.7.0` - SVG to PNG conversion
- `python-dotenv>=1.0.0` - Environment management
- `tqdm>=4.66.0` - Progress bars
- `pytest>=7.4.0` - Testing framework
- `requests>=2.31.0` - HTTP library

---

## Development Notes

### Code Style

- Max 300 lines per file (modularization preferred)
- Max 30 lines per function
- Extensive commenting with format: "This uses A to do B so that C. Used in D."
- camelCase for variables/functions (no underscores)
- No single-character variable names

### Markdown Formatting

- MD012: No multiple blank lines
- MD022: Blank lines around headings
- MD031: Blank lines around code blocks
- MD001: Incremental heading levels
- MD032: Blank lines around lists

---

## Change Log

### 2025-09-30 21:00

**Core Implementation Complete**:
- Created `src/config.py` (175 lines) - Configuration management
- Created `src/convert_svg_to_png.py` (158 lines) - SVG to PNG converter
- Created `src/create_notion_db.py` (210 lines) - Database creator
- Created `src/analyze_icons.py` (299 lines) - Gemini icon analyzer
- Created `src/upload_to_notion.py` (285 lines) - Notion uploader
- Created `Makefile` for CLI automation
- All modules import successfully
- All modules under 300 line limit
- Code style compliance verified

### 2025-09-30 19:00

**Initial Setup**:
- Initial project setup
- README.md created with implementation plan
- Progress log structure defined
- Virtual environment created and dependencies installed
- GitHub repository created: https://github.com/FalkSinke/notion-icon-analyzer
- Project structure scaffolded with src/, tests/, output/, png_icons/ directories
- Configuration files created (.env, .env.example, .gitignore)
- Initial commit and push to GitHub

---

## Next Steps

1. **Configure API Keys**: Add Gemini and Notion API keys to `.env`
2. **Set Up Hosting**: Configure ICON_BASE_URL for PNG hosting
3. **Test Conversion**: Run `make convert` on small subset
4. **Create Database**: Run `make create-db` to initialize Notion
5. **Test Analysis**: Analyze 5-10 icons to verify prompt
6. **Full Pipeline**: Execute `make all` for complete processing

---

## License

Internal project - Not for public distribution

---

## Contact

For questions or issues, contact the development team.
