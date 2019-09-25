#!/usr/bin/env python
# coding: utf-8

# run this first, then pubsFromBib.py and direct output to ../_pubs.yml

from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re
import json
import sys

conffname = 'conferences.json'
if os.path.exists(conffname):
    with open(conffname, 'r') as jsonfile:
        conference_names = json.load(jsonfile)

codeffname = 'code-urls.json'
if os.path.exists(codeffname):
    with open(codeffname, 'r') as jsonfile:
        code_urls = json.load(jsonfile)

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

parser = bibtex.Parser()
dblpbib = parser.parse_file("dblp.bib")
allbib = parser.parse_file("addendum.bib") # returns the union

print("papers:\n", end="")

for bib_id in sorted(allbib.entries, reverse=True,
        key=lambda bib_id: allbib.entries[bib_id].fields["year"]+bib_id):
    e = allbib.entries[bib_id]
    b = e.fields
    
    try:
        authors = ""
        num_authors = len(e.persons["author"])
        for ai, author in enumerate(e.persons["author"]):
            if ai == (num_authors-1) and num_authors != 1:
                authors += "and "
            authors += html_escape(author.first_names[0].replace("{", "").replace("}","").replace("\\","")) + " " + html_escape(author.last_names[0].replace("{", "").replace("}","").replace("\\","")) 
            if ai < (num_authors-2):
                authors += ", "
            elif ai < (num_authors-1):
                authors += " "
        paper_type = e.type

        ## YAML variables
        md  = "  - layout: paper" + "\n"
        md += "    author: \"" + authors + "\"\n"
        md += "    title: \""   + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + '"\n'
        md += "    year: \"" + b["year"] + "\"\n"
        md += "    paper-type: " + paper_type + "\n"

        if paper_type == "inproceedings":
            # find the short name of the conference
            name = None
            if 'confid' in b:
                proc = conference_names.get(b.get("confid"))
                if proc: name = proc['short']
            elif 'confname' in b:
                name = b['confname']

            if not name:
                print('WARNING: no entry for conference', b['booktitle'], file=sys.stderr)
                name = b['booktitle']

            name = html_escape(name.replace("{", "").replace("}","").replace("\\","")) 
            
            md += "    booktitle: \"" + name + "\"\n"

        elif paper_type == "article":
            name = html_escape(b['journal'].replace("{", "").replace("}","").replace("\\","")) 
            md += "    journal: \"" + name + "\"\n"
            if "volume" in b.keys():
                md += "    volume: " + b["volume"] + "\n"
            # could have number, issue, month

        #optional doc and code url
        if "url" in b.keys():
            if len(str(b["url"])) > 5:
                md += "    docurl: \"" + b["url"].replace("\\","") + "\"\n"

        codeurl = code_urls.get(bib_id)
        if codeurl:
            md += "    codeurl: \"" + codeurl['url'] + "\"\n"

        #optional page numbers
        #if "pages" in b.keys():
            #md += "    pages: " + b["pages"].replace("--", "&mdash;") + "\n"

        print(md, end="")

    except KeyError as e:
        print("WARNING Missing Expected Field", e, "from entry ", bib_id, ": \"", b["title"][:30] ,"\"", file=sys.stderr)
        continue
