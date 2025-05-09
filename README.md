# PDF‑to‑Markdown

Convert PDFs into clean, structured **Markdown** files that can be uploaded directly to OpenWebUI’s **Knowledge** base for Retrieval‑Augmented Generation (RAG).

---

## ✨ Features
- Uses **[PyMuPDF4LLM](https://pypi.org/project/pymupdf4llm/)** to preserve headings, lists, tables, and code blocks.
- Processes every PDF in `pdfs/` and writes a matching `.md` file to `markdown/`.
- Skips corrupted/problematic PDFs without stopping the batch.
- Bundles all Markdown files into `markdown.zip` for one‑click import in OpenWebUI.

---

## 🚀 Quick Start

```bash
pip install --upgrade pip
pip install pymupdf4llm           # pulls in PyMuPDF automatically

mkdir pdfs                         # drop your PDFs here
python convert_pdf_to_md.py        # outputs to markdown/ + zip archive
```
