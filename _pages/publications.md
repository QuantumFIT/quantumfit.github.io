---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---

{% include base_path %}

{% if site.publications.size > 0 %}
  {% for post in site.publications reversed %}
    {% include archive-single.html %}
  {% endfor %}
{% else %}
_No publications listed yet. Add one Markdown file per publication to the `_publications/` directory -- see the [academicpages publication format](https://academicpages.github.io/markdown/) for the front matter fields it expects (title, venue, date, excerpt, citation, paperurl, ...)._
{% endif %}
