import bibtexparser
import subprocess
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def create_bibtex(entrytype, contents):
    print("creating", entrytype)
    db = BibDatabase()
    entry = None

    if entrytype == "doi":
        # TODO
        return None
    
    elif entrytype == "book":
        print("AAAAAAAAAAAAAAA", contents)
        entry = {
            'ENTRYTYPE': entrytype,
            'ID': contents[1],
            'author': contents[2],
            'title': contents[3],
            'booktitle': contents[4],
            'publisher': contents[5],
            'year': str(contents[6])
        }
    elif entrytype == "article":
        entry = {
            'ENTRYTYPE': entrytype,
            'ID': contents[1],
            'author': contents[2],
            'title': contents[3],
            'journal': contents[4],
            'year': str(contents[5])
        }
    elif entrytype == "inproceeding":
        entry = {
            'ENTRYTYPE': entrytype,
            'ID': contents[1],
            'author': contents[2],
            'title': contents[3],
            'booktitle': contents[4],
            'year': str(contents[5])
        }

    db.entries = [entry]
    writer = BibTexWriter()
    bibtex_string = writer.write(db)

    return bibtex_string


def convert_to_bibtex(doi):
    # Use subprocess to call the 'doi2bib' command
    try:
        result = subprocess.run(
            ['doi2bib', doi],
            check=True,  # Raise an exception if the command fails
            stdout=subprocess.PIPE,  # Capture the standard output
            stderr=subprocess.PIPE  # Capture the standard error
        )
        # Return the BibTeX result
        return result.stdout.decode('utf-8')  # Convert bytes to string
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode('utf-8')}")
        return None


def append_bibtex_entry(file_path, entry_str):
    with open(file_path, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    new_database = bibtexparser.loads(entry_str)

    bib_database.entries.extend(new_database.entries)

    writer = BibTexWriter()
    with open(file_path, 'w') as bibtex_file:
        bibtex_file.write(writer.write(bib_database))


def read_bibtex_file(file):
    with open(file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    print(bib_database.entries)
