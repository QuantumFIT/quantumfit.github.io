---
layout: archive
title: "News"
permalink: /news/
author_profile: false
---

{% include base_path %}

{% if site.posts.size > 0 %}
  {% for post in site.posts %}
    {% include archive-single.html %}
  {% endfor %}
{% else %}
_No news posted yet. Add one Markdown file per item to the `_posts/` directory, named `YYYY-MM-DD-title.md`._
{% endif %}
