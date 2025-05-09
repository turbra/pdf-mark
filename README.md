# pdf‑to‑markdown

Turn **any** PDF into tidy, developer‑friendly **Markdown** in one command. Perfect for feeding Large‑Language‑Model (LLM) knowledge bases such as **OpenWebUI**, **LlamaIndex/LangChain** pipelines, or plain documentation sites.

---

## ✨ Key Features

| Feature                      | Details                                                                                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **High‑fidelity conversion** | Powered by **[PyMuPDF4LLM](https://pypi.org/project/pymupdf4llm/)** ‑ preserves headings (`#`), lists, tables, and code fences straight from the PDF layout. |
| **Single dependency**        | No heavy toolchain or external binaries ‑ just one PyPI package.                                                                                             |
| **CLI arguments**            | `--input`, `--output`, and `--zip` flags so you never edit the script.                                                                                       |
| **Recursive scanning**       | Walks sub‑folders so you can drop PDFs in a tree.                                                                                                            |
| **Incremental runs**         | Skips PDFs that already have an up‑to‑date `.md` file.                                                                                                       |
| **Graceful error handling**  | Logs bad PDFs but keeps going. Returns non‑zero exit code if *nothing* converts.                                                                             |
| **One‑click bundle**         | Creates a ready‑to‑upload ZIP (default `markdown.zip`).                                                                                                      |

---

## 🛠 Requirements

* Python 3.9 or newer (3.10‑3.12 tested)
* `pip install pymupdf4llm`

> **Note ✏️**  If you run on Alpine or another distro without a pre‑built wheel, you may need build tools (`build‑essential`, `python3‑dev`).

---

## 🚀 Quick Start

```bash
# 1 / install the single requirement
$ pip install --upgrade pip
$ pip install pymupdf4llm

# 2 / drop PDFs anywhere under ./pdfs
$ mkdir -p pdfs && mv ~/Downloads/*.pdf pdfs/

# 3 / convert
$ python convert.py            # uses defaults (./pdfs, ./markdown, markdown.zip)

# 4 / upload markdown.zip to OpenWebUI → Knowledge or import into your own RAG pipeline 🎉
```

### Custom paths

```bash
python convert.py \
  --input  /path/to/my/pdfs \
  --output /tmp/md_out \
  --zip    docs_md.zip
```

---

## 📂 Folder Layout (after a run)

```
.
├─ convert.py        # the script
├─ pdfs/                       # your source PDFs (can be nested)
├─ markdown/                   # auto‑generated .md files
└─ markdown.zip                # everything bundled
```

---

## 💡 How it Works

1. Walk the input directory (recursively).
2. For each `*.pdf`, call `pymupdf4llm.to_markdown()`.
3. Write a UTF‑8 `.md` file with the same base name.
4. Skip reconversion if the Markdown is newer than the PDF.
5. When finished, ZIP all Markdown files for convenience.
