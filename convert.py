#!/usr/bin/env python3
import os, zipfile, argparse, sys
import pymupdf4llm

def convert_pdf(pdf_path: str) -> str:
    """Return markdown string from a PDF (raises on failure)."""
    return pymupdf4llm.to_markdown(pdf_path)

def main() -> None:
    ap = argparse.ArgumentParser(description="Convert PDFs to Markdown and bundle them.")
    ap.add_argument("-i", "--input",  default="./pdfs",     help="input directory with PDFs")
    ap.add_argument("-o", "--output", default="./markdown", help="output directory for .md files")
    ap.add_argument("-z", "--zip",    default="markdown.zip", help="zip file name")
    args = ap.parse_args()

    os.makedirs(args.output, exist_ok=True)
    converted = 0

    for root, _, files in os.walk(args.input):
        for fname in files:
            if not fname.lower().endswith(".pdf"):
                continue
            pdf_path = os.path.join(root, fname)
            md_out   = os.path.join(
                args.output,
                os.path.splitext(fname)[0] + ".md"
            )
            # skip up‑to‑date conversions
            if os.path.exists(md_out) and os.path.getmtime(md_out) >= os.path.getmtime(pdf_path):
                continue
            try:
                md = convert_pdf(pdf_path)
            except Exception as e:
                print(f"[ERROR] {fname}: {e}")
                continue
            with open(md_out, "w", encoding="utf-8") as f:
                f.write(md)
            converted += 1
            print(f"✓ {fname} → {md_out}")

    if converted == 0:
        print("No PDFs converted.")
    else:
        with zipfile.ZipFile(args.zip, "w", zipfile.ZIP_DEFLATED) as z:
            for md_file in os.listdir(args.output):
                z.write(os.path.join(args.output, md_file), md_file)
        print(f"📦 Archive ready: {args.zip}")

    sys.exit(0 if converted else 1)

if __name__ == "__main__":
    main()
