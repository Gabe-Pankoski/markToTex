# markToTex

Convert Markdown files to PDF via LaTeX.

## Dependencies

### System

- **pandoc** — used by `pypandoc` for Markdown-to-LaTeX conversion
- **pdflatex** — part of a LaTeX distribution (e.g. TeX Live, MiKTeX)

Install on Arch Linux:

```sh
sudo pacman -S pandoc texlive-basic texlive-latex
```

### Python

- **pypandoc** — Python bindings for pandoc (declared in `pyproject.toml`)

Requires Python >= 3.14.

## Installation

```sh
uv sync
```

## Usage

```sh
uv run mark-to-tex <input.md> [-o output.pdf] [--keep-tex]
```

- `<input.md>` — path to the Markdown file
- `-o, --output` — output PDF path (default: same name as input with `.pdf` extension)
- `--keep-tex` — keep the intermediate `.tex` file after compilation
