---
permalink: /about/
layout: page
title: About QuantumFIT
description: A brief introduction to the QuantumFIT research group and this website.
comments: false
modified: 2026-08-28
breadcrumbs: true
---

**QuantumFIT** is the Quantum Computing Systems research group at the [Faculty of Information Technology](https://www.fit.vut.cz/), [Brno University of Technology](https://www.vut.cz/), working on quantum computing and quantum software engineering.

<!-- TODO: replace this placeholder paragraph with a real description of the group's research focus. -->

## Contact

{% assign c = site.data.positions.contact %}
{% if c.url %}[**{{ c.name }}**]({{ c.url }}){% else %}**{{ c.name }}**{% endif %}, {{ c.role }}
&middot; [{{ c.email }}](mailto:{{ c.email }})

### Postal address

{% comment %}
  Rendered as an <address> so each line stands on its own instead of running
  together into a paragraph. font-style is reset because browsers italicise
  <address> by default. No e-mail address here on purpose -- see
  _data/positions.yml.
{% endcomment %}
<address style="font-style: normal; line-height: 1.6;">
{% for line in site.data.positions.postal.lines %}{{ line }}{% unless forloop.last %}<br>{% endunless %}
{% endfor %}</address>

{% if site.data.positions.postal.url %}[{{ site.data.positions.postal.url | remove: "https://" | remove: "/" }}]({{ site.data.positions.postal.url }}){% endif %}
