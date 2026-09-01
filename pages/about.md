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
  Two cards side by side: how to reach a person, and where to send post.
  They reuse .member-grid / .member-card / .member-info from the Team page, so
  the styling and the dark-mode rules in _sass/_dark.scss already cover them.

  Links are written as raw <a> rather than markdown, which avoids needing
  markdown="1" on the description divs -- and with it the kramdown rule that
  every tag must start at column 0 or the closing </div>s get swallowed into
  the paragraph above.

  The name links to the e-mail address. The link to the PI's own page is
  deliberately absent; it lives only on the Team page (bio_link in group.yml).
{% endcomment %}
{% assign c = site.data.positions.contact %}
<div class="member-grid">
<div class="member-card">
<div class="member-info">
<h4>Contact person</h4>
<div class="member-description">
<a href="mailto:{{ c.email }}"><strong>{{ c.name }}</strong></a><br>
<a href="mailto:{{ c.email }}">{{ c.email }}</a>{% if c.web %}<br>
<a href="{{ c.web }}">{{ c.web_label | default: c.web }}</a>{% endif %}
</div>
</div>
</div>
<div class="member-card">
<div class="member-info">
<h4>Postal address</h4>
<div class="member-description">
{% comment %}
  An <address> so each line stands on its own instead of running together into
  a paragraph. font-style is reset because browsers italicise it by default.
  No e-mail address here on purpose -- see _data/positions.yml.
{% endcomment %}
<address style="font-style: normal; line-height: 1.6; margin: 0;">
{{ c.name }}<br>
{% for line in site.data.positions.postal.lines %}{{ line }}{% unless forloop.last %}<br>{% endunless %}
{% endfor %}</address>
</div>
</div>
</div>
</div>
