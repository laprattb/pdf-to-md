#!/usr/bin/env python3
"""
PDF to Markdown Converter

Converts PDF documents to Markdown format, preserving text structure,
tables, and optionally extracting images.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

try:
    import pymupdf4llm
except ImportError:
    print("Error: pymupdf4llm is required. Install with: pip install pymupdf4llm")
    sys.exit(1)


def convert_pdf_to_markdown(
    pdf_path: str,
    output_path: Optional[str] = None,
    pages: Optional[List[int]] = None,
    extract_images: bool = False,
    image_dir: Optional[str] = None,
) -> str:
    """
    Convert a PDF file to Markdown format.

    Args:
        pdf_path: Path to the input PDF file
        output_path: Optional path for the output Markdown file
        pages: Optional list of page numbers to convert (0-indexed)
        extract_images: Whether to extract images from the PDF
        image_dir: Directory to save extracted images

    Returns:
        The Markdown content as a string
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    kwargs = {}
    if pages is not None:
        kwargs["pages"] = pages
    if extract_images:
        kwargs["write_images"] = True
        if image_dir:
            kwargs["image_path"] = image_dir
        else:
            kwargs["image_path"] = str(pdf_path.parent / f"{pdf_path.stem}_images")

    markdown_content = pymupdf4llm.to_markdown(str(pdf_path), **kwargs)

    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown_content, encoding="utf-8")
        print(f"Markdown saved to: {output_path}")

    return markdown_content


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF documents to Markdown format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.pdf                     # Output to stdout
  %(prog)s document.pdf -o output.md        # Save to file
  %(prog)s document.pdf -p 0 1 2            # Convert only first 3 pages
  %(prog)s document.pdf --images            # Extract images too
        """,
    )
    parser.add_argument("pdf", help="Path to the PDF file to convert")
    parser.add_argument("-o", "--output", help="Output Markdown file path")
    parser.add_argument(
        "-p",
        "--pages",
        type=int,
        nargs="+",
        help="Page numbers to convert (0-indexed)",
    )
    parser.add_argument(
        "--images",
        action="store_true",
        help="Extract images from the PDF",
    )
    parser.add_argument(
        "--image-dir",
        help="Directory to save extracted images",
    )

    args = parser.parse_args()

    try:
        result = convert_pdf_to_markdown(
            pdf_path=args.pdf,
            output_path=args.output,
            pages=args.pages,
            extract_images=args.images,
            image_dir=args.image_dir,
        )
        if not args.output:
            print(result)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error converting PDF: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
