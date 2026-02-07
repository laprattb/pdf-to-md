# PDF to Markdown Converter

A Python utility that converts PDF documents to Markdown format using `pymupdf4llm`, preserving text structure and tables.

## Project Structure

```
pdf-to-md/
├── pdf_to_md.py      # Main conversion script
├── requirements.txt  # Dependencies (pymupdf4llm)
├── pdfs/             # Source PDFs (product documentation)
│   └── [subfolders]  # Organized by product/category
└── mds/              # Output markdown files (mirrors pdfs/ structure)
```

## Environment

Always use the virtual environment:
```bash
.venv\Scripts\python pdf_to_md.py [args]
```

## Usage

### Batch conversion (recommended)
```bash
# Convert all PDFs in pdfs/ to mds/, preserving folder structure
.venv\Scripts\python pdf_to_md.py pdfs -o mds --batch

# With image extraction
.venv\Scripts\python pdf_to_md.py pdfs -o mds --batch --images
```

### Single file conversion
```bash
# Output to stdout
.venv\Scripts\python pdf_to_md.py pdfs/document.pdf

# Save to file
.venv\Scripts\python pdf_to_md.py pdfs/document.pdf -o mds/document.md

# Convert specific pages (0-indexed)
.venv\Scripts\python pdf_to_md.py pdfs/document.pdf -p 0 1 2 -o mds/document.md

# Extract images
.venv\Scripts\python pdf_to_md.py pdfs/document.pdf -o mds/document.md --images --image-dir mds/images
```

### As a module
```python
from pdf_to_md import convert_pdf_to_markdown

markdown = convert_pdf_to_markdown("pdfs/document.pdf")
convert_pdf_to_markdown("pdfs/document.pdf", output_path="mds/document.md")
```

## CLI Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output Markdown file path (or directory with --batch) |
| `-p, --pages` | Page numbers to convert (0-indexed, single file only) |
| `--images` | Extract images from the PDF |
| `--image-dir` | Directory to save extracted images (single file only) |
| `--batch` | Batch convert all PDFs in source directory |
| `-f, --force` | Overwrite existing output files (default: skip) |

## Workflow

PDFs in `/pdfs` are converted to Markdown in `/mds`, preserving the folder structure:
- `pdfs/opint/manual.pdf` -> `mds/opint/manual.md`
- `pdfs/umc/guide.pdf` -> `mds/umc/guide.md`

## Dependencies

- `pymupdf4llm>=0.0.27` - PDF parsing and markdown conversion
