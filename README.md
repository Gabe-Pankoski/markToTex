# markToTex

Convert Markdown files to PDF via LaTeX.

## System Dependencies

These must be installed on your system before using markToTex. They are **not** installed automatically by pip or pipx.

### pandoc

Used by `pypandoc` to convert Markdown to LaTeX.

| OS | Command |
|----|---------|
| Arch Linux | `sudo pacman -S pandoc` |
| Ubuntu / Debian | `sudo apt install pandoc` |
| Fedora | `sudo dnf install pandoc` |
| macOS (Homebrew) | `brew install pandoc` |

### pdflatex (TeX Live / MiKTeX)

Used to compile the intermediate `.tex` file into a PDF.

| OS | Command |
|----|---------|
| Arch Linux | `sudo pacman -S texlive-basic texlive-latex` |
| Ubuntu / Debian | `sudo apt install texlive texlive-latex-extra` |
| Fedora | `sudo dnf install texlive-scheme-basic` |
| macOS (Homebrew) | `brew install --cask mactex-no-gui` |

> **Note:** Minimal TeX Live installs may lack packages needed to render certain Markdown constructs. If you see `pdflatex` errors about missing `.sty` files, install `texlive-latex-recommended` (Debian/Ubuntu) or the appropriate `texlive-*` package for your distro.

## Installation

### pipx (recommended for CLI use)

```sh
pipx install git+https://github.com/USERNAME/markToTex.git
```

Or from a local clone:

```sh
pipx install .
```

### uv (for development)

```sh
uv sync
```

## Usage

### After pipx install

```sh
mark-to-tex <input.md> [-o output.pdf] [--keep-tex]
```

### With uv

```sh
uv run mark-to-tex <input.md> [-o output.pdf] [--keep-tex]
```

### Options

| Flag | Description |
|------|-------------|
| `<input.md>` | Path to the Markdown file (required) |
| `-o, --output` | Output PDF path (default: same name as input with `.pdf` extension) |
| `--keep-tex` | Keep the intermediate `.tex` file after compilation |
