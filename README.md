# PDF to Markdown Converter

A Python utility to convert PDF documents to Markdown format, preserving text structure and tables.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Output to stdout
python pdf_to_md.py document.pdf

# Save to file
python pdf_to_md.py document.pdf -o output.md

# Convert specific pages (0-indexed)
python pdf_to_md.py document.pdf -p 0 1 2

# Extract images
python pdf_to_md.py document.pdf -o output.md --images --image-dir ./images
```

## Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output Markdown file path |
| `-p, --pages` | Page numbers to convert (0-indexed) |
| `--images` | Extract images from the PDF |
| `--image-dir` | Directory to save extracted images |

## As a Module

```python
from pdf_to_md import convert_pdf_to_markdown

markdown = convert_pdf_to_markdown("document.pdf")

# Or save directly to file
convert_pdf_to_markdown("document.pdf", output_path="output.md")
```
