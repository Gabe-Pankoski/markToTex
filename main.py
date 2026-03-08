import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pypandoc


def convert_md_to_tex(md_path: Path, tex_path: Path) -> None:
    pypandoc.convert_file(
        str(md_path),
        "latex",
        outputfile=str(tex_path),
        extra_args=["--standalone"],
    )


def compile_tex_to_pdf(tex_path: Path, pdf_output: Path) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_tex = Path(tmpdir) / "document.tex"
        shutil.copy(tex_path, tmp_tex)

        for _ in range(2):  # run twice to resolve references
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "document.tex"],
                cwd=tmpdir,
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print(result.stdout[-3000:], file=sys.stderr)
                print(result.stderr[-1000:], file=sys.stderr)
                sys.exit(1)

        tmp_pdf = Path(tmpdir) / "document.pdf"
        if not tmp_pdf.exists():
            print("Error: pdflatex succeeded but produced no PDF.", file=sys.stderr)
            sys.exit(1)

        shutil.copy(tmp_pdf, pdf_output)


def main():
    parser = argparse.ArgumentParser(description="Convert a Markdown file to PDF via LaTeX")
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument("-o", "--output", help="Output PDF path (default: input stem + .pdf)")
    parser.add_argument("--keep-tex", action="store_true", help="Keep intermediate .tex file")
    args = parser.parse_args()

    md_path = Path(args.input).resolve()
    if not md_path.exists():
        print(f"Error: '{md_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if md_path.stat().st_size == 0:
        print(f"Error: '{md_path}' is empty.", file=sys.stderr)
        sys.exit(1)

    pdf_path = Path(args.output).resolve() if args.output else md_path.with_suffix(".pdf")
    tex_path = pdf_path.with_suffix(".tex")

    print(f"Converting {md_path.name} -> {tex_path.name} ...")
    convert_md_to_tex(md_path, tex_path)

    print(f"Compiling {tex_path.name} -> {pdf_path.name} ...")
    compile_tex_to_pdf(tex_path, pdf_path)

    if not args.keep_tex:
        tex_path.unlink(missing_ok=True)

    print(f"Done: {pdf_path}")


if __name__ == "__main__":
    main()
