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

{% for org in site.data.positions %}
**{{ org.title }}**{% if org.department %}, {{ org.department }}{% endif %}
{% if org.address %}{{ org.address }}{% endif %}{% if org.location %}, {{ org.location }}{% endif %}
{% if org.email %}Email: [{{ org.email }}](mailto:{{ org.email }}){% endif %}
{% endfor %}
