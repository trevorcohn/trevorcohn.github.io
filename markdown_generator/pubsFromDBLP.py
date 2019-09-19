#!/usr/bin/env python
# coding: utf-8

import re
import os
import urllib.request
import ssl
from pybtex.database.input import bibtex
import pybtex.database
import pybtex.database.input.bibtex
import pybtex.errors 
import pybtex.utils
import numpy as np
import csv
import json

# step 1: download from DBLP, filter out CoRR papers [what about papers that are under review / preprints?]

dblp_url = 'https://dblp.uni-trier.de/pers/tb2/c/Cohn:Trevor.bib'
#dblp_url = 'https://dblp.org/pers/tb2/f/Frermann:Lea.bib'
#dblp_url = 'https://dblp.org/pers/tb2/l/Lau:Jey_Han.bib'
#dblp_url = 'https://dblp.org/pers/tb2/b/Baldwin:Timothy.bib'
#dblp_url = 'https://dblp.org/pers/tb2/v/Verspoor:Karin_M=.bib'
#dblp_url = 'https://dblp.org/pers/tb2/b/Beck:Daniel.bib'

context = ssl._create_unverified_context()
with urllib.request.urlopen(dblp_url, context=context) as response:
   html = response.read().decode('utf-8')

pybtex.errors.set_strict_mode(False)
parser = bibtex.Parser()
bibdata = parser.parse_string(html)

conference_names = {}
conffname = 'conferences.json'
if os.path.exists(conffname):
    with open(conffname, 'r') as jsonfile:
        conference_names = json.load(jsonfile)

#loop through the individual references in a given bibtex file
to_keep = pybtex.database.BibliographyData()
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields

    try:
        paper_type = bibdata.entries[bib_id].type

        if paper_type not in ['inproceedings', 'article']: # fixme book, chapter etc?
            continue

        if b.get('journal') == "CoRR": 
            continue

        if paper_type == 'inproceedings':
            new_entry = pybtex.database.Entry(paper_type, persons=bibdata.entries[bib_id].persons)
            for f in "author title booktitle year pages url biburl".split():
                if f in b: new_entry.fields[f] = b[f]

            new_entry.fields['confid'] = b['crossref']

            conf = conference_names.get(b['crossref'])
            if conf != None:
                proceedings = conf['long']
                short = conf['short']
            else:
                proc = new_entry.fields['booktitle']
                print('WARNING: guessing details of unseen conference:', b['crossref'])
                parts = proc.split(',')
                lengths = list(map(str.__len__, parts))
                longest = np.argmax(lengths)

                proceedings = parts[longest].strip()
                new_entry.fields['booktitle'] = proceedings

                # see if there's a short form in the string
                short = None
                if longest >= 1:
                    candidate = parts[longest-1]
                    if len(candidate) >= 3 and len(list(filter(str.islower, candidate))) <= 1:
                        short = candidate.strip()

                if not short:
                    # may be longest+1
                    candidate = parts[longest+1]
                    if len(candidate) >= 3 and len(list(filter(str.islower, candidate))) <= 1:
                        short = candidate.strip()

                if not short:
                    match = re.search(r'{([^}]+)}( {([^}]+)})?\s?[0-9]*,', proc)
                    if match:
                        short = match.group(1)
                        if match.group(3):
                            short += ' '  + match.group(3)

                print('\tlong form', proceedings)
                print('\tshort form', short)

                conference_names[b['crossref']] = { 'long': proceedings, 'short': short }

            new_entry.fields['booktitle'] = proceedings
            if short:
                new_entry.fields['confname'] = short

            to_keep.entries[bib_id] = new_entry

        elif paper_type == 'article':
            new_entry = pybtex.database.Entry(paper_type, persons=bibdata.entries[bib_id].persons)
            for f in "author title journal year volume number month issue pages url doi biburl".split():
                if f in b: new_entry.fields[f] = b[f]
            to_keep.entries[bib_id] = new_entry
            

    except KeyError as e:
        print("WARNING Missing Expected Field", e, "from entry ", bib_id, ": \"", b["title"][:30] ,"\"")
        continue

to_keep.to_file("dblp.bib", "bibtex")

if not os.path.exists(conffname):
    with open(conffname, "w") as conffile:
        json.dump(conference_names, conffile, indent=2, sort_keys=True)
    
