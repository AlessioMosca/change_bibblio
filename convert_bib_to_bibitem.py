import tkinter as tk
from tkinter import filedialog
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

def load_bibtex_file(filename):
    """ Load the BibTeX file. """
    with open(filename, 'r') as bibfile:
        parser = BibTexParser()
        parser.customization = convert_to_unicode
        bib_database = parser.parse_file(bibfile)
    return bib_database

def generate_bibitem(entries):
    """ Generate LaTeX \bibitem entries from BibTeX entries. """
    bibitems = []
    for entry in entries.entries:
        author = entry.get('author', '')
        year = entry.get('year', '')
        title = entry.get('title', '')
        journal = entry.get('journal', '')
        volume = entry.get('volume', '')
        number = entry.get('number', '')
        pages = entry.get('pages', '')
        publisher = entry.get('publisher', '')

        # Handle each type of BibTeX entry
        if entry.get('type') == 'article':
            bibitem = f"\\bibitem{{{entry.get('ID')}}}\n"
            bibitem += f"{author}, ``{title},'' {journal}, vol. {volume}, no. {number}, pp. {pages}, {year}.\n"
        elif entry.get('type') == 'book':
            bibitem = f"\\bibitem{{{entry.get('ID')}}}\n"
            bibitem += f"{author}, \\textit{{{title}}}, {publisher}, {year}.\n"
        elif entry.get('type') == 'inproceedings':
            bibitem = f"\\bibitem{{{entry.get('ID')}}}\n"
            bibitem += f"{author}, ``{title},'' in \\textit{{{journal}}}, {year}.\n"
        else:
            bibitem = f"\\bibitem{{{entry.get('ID')}}}\n"
            bibitem += f"{author}, ``{title},'' {journal}, {year}.\n"

        bibitems.append(bibitem)
    return bibitems

def save_latex_file(entries, filename):
    """ Save the LaTeX \bibitem entries to a file. """
    with open(filename, 'w') as latexfile:
        latexfile.write("\\begin{thebibliography}{99}\n")
        for entry in entries:
            latexfile.write(entry)
        latexfile.write("\\end{thebibliography}\n")

def main():
    # Create a Tkinter root window (it will be hidden)
    root = tk.Tk()
    root.withdraw()

    # Open file dialog to select the input BibTeX file
    input_filename = filedialog.askopenfilename(
        title="Select the BibTeX file",
        filetypes=[("BibTeX files", "*.bib"), ("All files", "*.*")]
    )
    if not input_filename:
        print("No input file selected.")
        return

    # Load the existing BibTeX file
    bib_data = load_bibtex_file(input_filename)
    
    # Generate \bibitem entries
    bibitems = generate_bibitem(bib_data)
    
    # Open file dialog to select the output LaTeX file
    output_filename = filedialog.asksaveasfilename(
        title="Save the LaTeX file",
        defaultextension=".bib",
        filetypes=[("LaTeX files", "*.bib"), ("All files", "*.*")]
    )
    if not output_filename:
        print("No output file selected.")
        return

    # Save to a LaTeX file
    save_latex_file(bibitems, output_filename)
    print(f"File saved as {output_filename}")

if __name__ == "__main__":
    main()
