# Icon Analysis & Notion Upload System

Automated pipeline for analyzing 884 Notion icons using Gemini 2.5 Flash and uploading them to a Notion database with rich semantic metadata.

## Overview

This system processes SVG icons through a three-stage pipeline:
1. **Conversion**: SVG → PNG format for API compatibility
2. **Analysis**: Vision AI extracts visual and semantic metadata
3. **Upload**: Rate-limited batch upload to Notion database

**Total Icons**: 884 SVG files
**Expected Runtime**: 7-8 hours
**Rate Limit**: 2 requests/second to Notion API

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
│   ├── convert_svg_to_png.py
│   ├── analyze_icons.py
│   ├── create_notion_db.py
│   ├── upload_to_notion.py
│   └── config.py
├── tests/                  # Test suite
│   ├── test_conversion.py
│   ├── test_analysis.py
│   └── test_upload.py
├── venv/                   # Virtual environment
├── requirements.txt
├── .env                    # API keys (not committed)
└── README.md
```

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

### 1. Clone and Navigate
```bash
cd /Users/falksinke/dev/privateprojects/notion-projects/iconupload
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
Create `.env` file:
```env
GEMINI_API_KEY=your_gemini_api_key_here
NOTION_API_KEY=your_notion_integration_token_here
NOTION_DATABASE_ID=will_be_generated
ICON_SOURCE_DIR=/Users/falksinke/dev/privateprojects/notion-projects/iconupload/notion_icons
PNG_OUTPUT_DIR=/Users/falksinke/dev/privateprojects/notion-projects/iconupload/png_icons
```

---

## Usage

### Step 1: Convert SVG to PNG
```bash
python src/convert_svg_to_png.py
```
- Converts all 884 SVG files to PNG format
- Output: `png_icons/` directory
- Progress: Real-time with tqdm

### Step 2: Create Notion Database
```bash
python src/create_notion_db.py
```
- Creates database with predefined schema
- Updates `.env` with `NOTION_DATABASE_ID`
- Returns: Database URL

### Step 3: Analyze Icons with Gemini
```bash
python src/analyze_icons.py
```
- Batch processes icons through Gemini 2.5 Flash
- Output: `output/icon_analysis.json`
- Checkpoint: Saves progress every 50 icons
- Resume: Automatically continues from last checkpoint

### Step 4: Upload to Notion
```bash
python src/upload_to_notion.py
```
- Rate-limited upload (0.5 requests/second)
- Progress tracking with success/failure counts
- Resume: Continues from last uploaded icon
- Output: `output/failed_icons.log` for manual review

### Resume After Interruption
All scripts support automatic resume from checkpoint:
```bash
# Analysis resumes from last processed icon
python src/analyze_icons.py

# Upload resumes from last uploaded icon
python src/upload_to_notion.py
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
  "last_uploaded_index": 450,
  "failed_icons": ["icon-name-1.png", "icon-name-2.png"],
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
# All tests
pytest tests/ -v

# Specific test
pytest tests/test_conversion.py -v
```

---

## Progress Log

### Phase 1: Setup & Conversion
- [ ] Project structure created
- [ ] Virtual environment initialized
- [ ] Dependencies installed
- [ ] Configuration files created
- [ ] SVG to PNG conversion completed (0/884)

### Phase 2: Notion Database Setup
- [ ] Database schema defined
- [ ] Notion integration connected
- [ ] Database created and ID captured

### Phase 3: Icon Analysis
- [ ] Gemini API configured
- [ ] Analysis prompt refined
- [ ] Icons analyzed (0/884)
- [ ] Checkpoint system tested

### Phase 4: Upload to Notion
- [ ] Rate limiting implemented
- [ ] Upload logic tested
- [ ] Icons uploaded (0/884)
- [ ] Failed icons logged

### Phase 5: Verification
- [ ] Upload count verified
- [ ] Database quality checked
- [ ] Failed icons reviewed
- [ ] Final report generated

---

## Technical Details

### Rate Limiting
- **Notion API**: 0.5 seconds between requests (2/second limit)
- **Gemini API**: Respects tier limits (60 RPM on free tier)
- **Token Bucket**: Implemented for burst protection

### Memory Management
- Icons processed in batches of 50
- Incremental JSON saves to prevent data loss
- Memory-efficient streaming for file operations

### File Naming Convention
- Input: `icon-arrow-up.svg`
- PNG: `icon-arrow-up.png`
- Analysis key: `icon-arrow-up`

---

## Cost Estimate

- **Gemini 2.5 Flash**: Free tier sufficient (60 RPM)
- **Notion API**: Free tier sufficient (rate limits only)
- **Total Cost**: $0.00

---

## Troubleshooting

### Issue: SVG Conversion Fails
```bash
# Check cairosvg installation
pip install --upgrade cairosvg pillow
```

### Issue: Gemini API Rate Limit
```bash
# Script will automatically retry with backoff
# Or manually adjust batch size in config.py
```

### Issue: Notion Upload Timeout
```bash
# Check internet connection
# Verify Notion integration has database access
# Review failed_icons.log for specific errors
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

---

## Development Notes

### Code Style
- Max 300 lines per file (modularization preferred)
- Max 30 lines per function
- Extensive commenting assuming reader knows nothing
- No underscores in variable/function names
- No single-character variable names

### Markdown Formatting
- MD012: No multiple blank lines
- MD022: Blank lines around headings
- MD031: Blank lines around code blocks
- MD001: Incremental heading levels
- MD032: Blank lines around lists

---

## Change Log

### 2025-09-30
- Initial project setup
- README.md created with implementation plan
- Progress log structure defined

---

## License

Internal project - Not for public distribution

---

## Contact

For questions or issues, contact the development team.
