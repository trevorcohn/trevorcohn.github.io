from pybtex.database.input import bibtex
import pybtex.database.input.bibtex
import sys

parser = bibtex.Parser()
dblpbib = parser.parse_file("dblp.bib")
allbib = parser.parse_file("addendum.bib") # returns the union

for bib_id in sorted(allbib.entries, reverse=True,
        key=lambda bib_id: allbib.entries[bib_id].fields["year"]+bib_id):

    e = allbib.entries[bib_id]
    found = False
    pos = 'MID'
    for i, p in enumerate(e.persons['author']):
        if 'Cohn' in p.last_names:
            found = True
            if i == 0: pos = 'FIRST'
            elif i == len(e.persons['author'])-1:
                pos = 'LAST'
            break

    if found: 
        print(pos, e)
