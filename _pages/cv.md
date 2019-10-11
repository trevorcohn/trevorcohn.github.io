---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Education

* 2017: Ph.D, Melbourne University
* 2000: B.Eng. (Hons 1, Software), Melbourne University
* 2000: B.Comm., Melbourne University

## Appointments

* 2014-: Associate Professor
  * Melbourne University, School of Computing and Information Systems

* 2009-2013: Senior Lecturer
  * Sheffield University, Department of Computer Science

* 2006-2009: Research Fellow
  * Edinburgh University, School of Informatics
  * Supervisor: Mirella Lapata

## Grants

TBD

## Academic honours

TBD

## Invited talks

TBD
  
## Publications

### Journals

  <ol>{% for paper in site.data.papers.papers %}
	{% if paper.paper-type == "article" %}
	    {% include single-paper-cv.html %} 
	{% endif %}
  {% endfor %}</ol>

### Conferences and workshops

  <ol>{% for paper in site.data.papers.papers %}
	{% if paper.paper-type == "inproceedings" %}
	    {% include single-paper-cv.html %} 
	{% endif %}
  {% endfor %}</ol>

  
## Teaching

  {% include teaching-cv.html %}

## Supervision

  {% include supervision-cv.html %}
  
## Service and leadership

* Programme Chair for EMNLP 2020.
* Local Chair for ACL 2018.
* Action editor for TACL 2018-2020.
* Editorial board for Computational Linguistics, Computer Speech and Language (2016).
* Area Chair for ACL, EMNLP, COLING, NeurIPS, IJCAI (various years).
