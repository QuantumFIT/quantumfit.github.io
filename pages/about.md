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

{% comment %}
  The name links to the e-mail address, not to the PI's own page -- that link
  lives only on the Team page (bio_link in _data/group.yml). The address is
  spelled out underneath as well so it can be read and copied without hovering.
{% endcomment %}
{% assign c = site.data.positions.contact %}
[**{{ c.name }}**](mailto:{{ c.email }})<br>
[{{ c.email }}](mailto:{{ c.email }})

### Postal address

{% comment %}
  Rendered as an <address> so each line stands on its own instead of running
  together into a paragraph. font-style is reset because browsers italicise
  <address> by default. No e-mail address here on purpose -- see
  _data/positions.yml.
{% endcomment %}
<address style="font-style: normal; line-height: 1.6;">
{{ c.name }}<br>
{% for line in site.data.positions.postal.lines %}{{ line }}{% unless forloop.last %}<br>{% endunless %}
{% endfor %}</address>

{% if site.data.positions.postal.url %}[{{ site.data.positions.postal.url | remove: "https://" | remove: "/" }}]({{ site.data.positions.postal.url }}){% endif %}
