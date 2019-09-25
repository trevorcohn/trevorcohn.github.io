---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
news:
  - I am a Programme Co-Chair for EMNLP 2020, to be held in the Dominican Republic. Stay tuned for the call for papers.
  - We have <a href="publications">two papers</a> to appear at <a href="https://www.emnlp-ijcnlp2019.org">EMNLP 2019</a>
  - My group had <a href="publications">papers</a> at ICML, WWW, NAACL, ICASSP and ACL (x3) in 2019.
  - Our <a href="https://www.aclweb.org/anthology/P18-1181">Shakespearean sonnet generator</a> was covered by <a href="https://www.newscientist.com/article/2175301-ai-creates-shakespearean-sonnets-and-theyre-actually-quite-good/">New Scientist</a>, <a href="https://www.thetimes.co.uk/article/computers-produce-poetry-by-the-meter-vk80077zl">Times UK</a>, <a href="http://www.dailymail.co.uk/sciencetech/article-6000619/Can-spot-real-Shakespeare-sonnet-AI-learns-write-poetry.html">Daily Mail</a>, and others. More information can be found <a href="https://github.com/jhlau/deepspeare#media-coverage">here</a>.
---

Understanding of human language by computers has been a central goal of
Artificial Intelligence since its beginnings, with massive potential to improve
communication, provide better information access and automate basic human
tasks. My research focuses on technologies for automatic processing of human
language, with several applications including automatic translation (akin to
Google and Bing's translation tools). My core focus is on probabilistic machine
learning modelling of language applications, particularly handling uncertain or
partly observed data and structured prediction problems.

## News

<ul>
{% for item in page.news %}
  <li>{{ item }}</li>
{% endfor %}
</ul>
