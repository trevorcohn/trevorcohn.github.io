---
layout: page
title: "Publications"
---

  You can also find my articles on <a href="{{site.gscholar}}">my
  Google Scholar profile</a> or <a  href="{{ site.dblp }}"> my DBLP
  profile</a>. Code links are provided below, see also 
      <a  href="{{ site.github }}">my GitHub page</a>.


{% for yr in (2005..2021) reversed %}
## {{yr}}
{% include publications.html year=yr %}
{% endfor %}

## 2003
{% include publications.html year=2003 %}
