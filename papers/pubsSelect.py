#!/usr/bin/env python
# coding: utf-8

from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
import sys

to_find = set(sys.argv[1:])
assert(to_find)

parser = bibtex.Parser()
dblpbib = parser.parse_file("dblp.bib")
allbib = parser.parse_file("addendum.bib") # returns the union

to_keep = pybtex.database.BibliographyData()
for bib_id in sorted(allbib.entries, reverse=True,
        key=lambda bib_id: allbib.entries[bib_id].fields["year"]+bib_id):

    if bib_id in to_find:
        to_keep.entries[bib_id] = allbib.entries[bib_id]

print(to_keep.to_string("bibtex"))

