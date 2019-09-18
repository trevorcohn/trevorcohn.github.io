#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re

# step 1: download from DBLP, filter out CoRR papers [what about papers that are under review / preprints?]
https://dblp.uni-trier.de/pers/tb2/c/Cohn:Trevor.bib

# remove crossref, @proceedings entries, publisher, timestamp, biburl, bibsource
# mungle booktitle to grab just short conference name which is usually between 

# step 2: load up my additional publications


#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    "proceeding": {
        "file" : "/Users/tcohn/Google Drive/trevor-cohn.bib",
        "venuekey": "booktitle",
        "venue-pretext": "In the proceedings of ",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    }
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


for pubsource in publist:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])

    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        #reset default date
        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"
        
        b = bibdata.entries[bib_id].fields
        
        try:

            #if "selected" in b and b["selected"] == "1":
            if True:

                authors = ""
                num_authors = len(bibdata.entries[bib_id].persons["author"])
                for ai, author in enumerate(bibdata.entries[bib_id].persons["author"]):
                    if ai == (num_authors-1) and num_authors != 1:
                        authors += "and "
                    authors += author.first_names[0]+" "+author.last_names[0]
                    if ai < (num_authors-2):
                        authors += ", "
                    elif ai < (num_authors-1):
                        authors += " "
                paper_type = bibdata.entries[bib_id].type

                ## YAML variables
                md  = "  - layout: paper" + "\n"
                md += "    author: \"" + authors + "\"\n"
                md += "    title: \""   + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + '"\n'
                md += "    year: \"" + b["year"] + "\"\n"
                md += "    paper-type: " + paper_type + "\n"

                if paper_type == "inproceedings":
                    # find the short name of the conference
                    re.
                    
                    md += "    booktitle: \"" + b["booktitle"] + "\"\n"
                    if "address" in b.keys():
                        md += "    address: \"" + b["address"] + "\"\n"

                elif paper_type == "article":
                    md += "    journal: \"" + b["journal"] + "\"\n"
                    if "volume" in b.keys():
                        md += "    volume: " + b["volume"] + "\n"

                #venue
                #md += "    venue: " + b["venue"] + "\n"
                
                #optional doc and code url
                if "docurl" in b.keys():
                    if len(str(b["url"])) > 5:
                        md += "    docurl: \"" + b["url"] + "\"\n"

                if "codeurl" in b.keys():
                    if len(str(b["codeurl"])) > 5:
                        md += "    codeurl: \"" + b["codeurl"] + "\"\n"

                #optional page numbers
                if "pages" in b.keys():
                    md += "    pages: " + b["pages"].replace("--", "&mdash;") + "\n"

                print(md, end="")

        except KeyError as e:
            print("WARNING Missing Expected Field", e, "from entry ", bib_id, ": \"", b["title"][:30] ,"\"")
            continue
