---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% for year in (2003..2019) reversed %}

## {{year}}

{% include publications.html year={{year}} %}

{% endfor %}
