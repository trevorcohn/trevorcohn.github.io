---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D, Melbourne University, 2007 
* B.Eng. (Hons 1, Software), Melbourne University, 2000
* B.Comm., Melbourne University, 2000

Work experience
======
* 2014-: Associate Professor
  * Melbourne University, School of Computing and Information Systems

* 2009-2013: Senior Lecturer
  * Sheffield University, Department of Computer Science

* 2006-2009: Research Fellow
  * Edinburgh University, School of Informatics
  * Supervisor: Mirella Lapata
  
Publications
======
  <ol reversed>{% for paper in site.data.papers.papers %}
    {% include single-paper-cv.html %}
  {% endfor %}</ol>
  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Programme Chair for EMNLP 2020.
* Local Chair for ACL 2018.
* Action editor for TACL 2018-2020.
* Editorial board for Computational Linguistics, Computer Speech and Language (2016).
* Area Chair for ACL, EMNLP, COLING, NeurIPS, IJCAI (various years).
