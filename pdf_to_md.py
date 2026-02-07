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


def convert_directory(
    source_dir: str,
    output_dir: str,
    extract_images: bool = False,
    force: bool = False,
) -> int:
    """
    Convert all PDF files in a directory to Markdown, preserving folder structure.

    Args:
        source_dir: Source directory containing PDF files
        output_dir: Output directory for Markdown files
        extract_images: Whether to extract images from PDFs
        force: Overwrite existing files

    Returns:
        Number of files converted
    """
    source_path = Path(source_dir)
    output_path = Path(output_dir)

    if not source_path.exists():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    pdf_files = list(source_path.rglob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in {source_dir}")
        return 0

    converted = 0
    skipped = 0
    for pdf_file in pdf_files:
        relative_path = pdf_file.relative_to(source_path)
        md_path = output_path / relative_path.with_suffix(".md")

        if md_path.exists() and not force:
            print(f"Skipping (exists): {md_path}")
            skipped += 1
            continue

        image_dir = None
        if extract_images:
            image_dir = str(md_path.parent / f"{md_path.stem}_images")

        try:
            convert_pdf_to_markdown(
                pdf_path=str(pdf_file),
                output_path=str(md_path),
                extract_images=extract_images,
                image_dir=image_dir,
            )
            converted += 1
        except Exception as e:
            print(f"Error converting {pdf_file}: {e}", file=sys.stderr)

    print(f"\nConverted {converted}/{len(pdf_files)} files" + (f" (skipped {skipped})" if skipped else ""))
    return converted


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
  %(prog)s pdfs -o mds --batch              # Batch convert directory
        """,
    )
    parser.add_argument("pdf", help="Path to PDF file or source directory (with --batch)")
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
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Batch convert all PDFs in source directory to output directory",
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Overwrite existing output files (default: skip existing)",
    )

    args = parser.parse_args()

    try:
        if args.batch:
            if not args.output:
                print("Error: --batch requires -o/--output for destination directory", file=sys.stderr)
                sys.exit(1)
            convert_directory(
                source_dir=args.pdf,
                output_dir=args.output,
                extract_images=args.images,
                force=args.force,
            )
        else:
            if args.output and Path(args.output).exists() and not args.force:
                print(f"Skipping (exists): {args.output}")
                print("Use --force to overwrite")
                sys.exit(0)
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
