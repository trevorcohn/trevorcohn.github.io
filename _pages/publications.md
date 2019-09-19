---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% for yr in (2005..2019) reversed %}
## {{yr}}
{% include publications.html year=yr %}
{% endfor %}

## 2003
{% include publications.html year=2003 %}
