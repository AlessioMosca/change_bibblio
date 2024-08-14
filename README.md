# BibTeX to LaTeX Converter

## Description

This Python script converts a BibTeX file (`.bib`) into a LaTeX file with `\bibitem` entries. It provides a user-friendly interface using `tkinter` for file selection and utilizes `bibtexparser` to parse and convert the BibTeX data.

## Features

- **File Selection**: Easily select the input BibTeX file and specify the output LaTeX file using file dialogs.
- **BibTeX Parsing**: Converts BibTeX entries into LaTeX `\bibitem` format.
- **Output Generation**: Generates a LaTeX file containing formatted `\bibitem` entries for inclusion in a LaTeX document.

## Usage

1. Run the script.
2. Choose the input BibTeX file when prompted.
3. Specify the location and filename for the output LaTeX file.
4. The script creates a LaTeX file with `\bibitem` entries based on the BibTeX data.

## Dependencies

- **Python 3.x**: Ensure Python 3.x is installed.
- **bibtexparser**: For parsing BibTeX files.
- **tkinter**: For file dialogs (usually included with Python by default).

## Installation

Install the required Python package with:

```bash
pip install bibtexparser
