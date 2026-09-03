---
permalink: /about/
layout: page
title: About |QuantumFIT>
description: A brief introduction to the |QuantumFIT> research group and this website.
comments: false
modified: 2026-09-03
breadcrumbs: true
---

{% comment %}
  The pipe is escaped. Unescaped, kramdown reads it as a table cell separator
  and turns this paragraph into a one-row table, cells "**" and the rest --
  which is exactly what it did until this comment was written. Anywhere the
  group's name appears in markdown body text it needs the backslash; front
  matter, raw HTML and Liquid output outside markdown are unaffected.
{% endcomment %}
**\|QuantumFIT>** is the Quantum Computing Systems research group at the [Faculty of Information Technology](https://www.fit.vut.cz/), [Brno University of Technology](https://www.vut.cz/), working on quantum computing and quantum software engineering.

{% comment %}
  Prose here rather than the labelled list the home page uses, so the two
  complement each other instead of repeating. Everything below is traceable to
  pages/tools.md and pages/publications.md; nothing claims a result the record
  does not carry.
{% endcomment %}
Our work applies **formal methods to quantum computing**. The recurring idea is to
represent whole sets of quantum states symbolically, as tree automata, rather than
enumerating states one at a time: a question about a quantum circuit then becomes a
question about automata. That makes it possible to check a circuit against a
pre-/post-condition specification, or to search it for bugs, without ever
enumerating individual states. The same perspective extends from circuits to
quantum programs, and to families of circuits rather than single instances.

Alongside verification we work on **simulation**, using symbolic execution over
multi-terminal binary decision diagrams together with loop summarization, so that a
repeated block of gates is analysed once instead of being unrolled. Underneath both
sits the automata and logic the methods are built from: tree automata and their
level-synchronized extension, omega-automata, and logic and SMT solving.

Two tools carry this into practice --- [AutoQ](/tools/), a verifier for quantum
circuits and programs, and [Medusa](/tools/), a simulator --- and the results behind
them appear in our [publications](/publications/), at PLDI, POPL, CAV, TACAS and
ICCAD.

## Contact

{% comment %}
  Two cards side by side: how to reach a person, and where to send post.
  They reuse .member-grid / .member-card / .member-info from the Team page, so
  the styling and the dark-mode rules in _sass/_dark.scss already cover them.

  Links are written as raw <a> rather than markdown, which avoids needing
  markdown="1" on the description divs -- and with it the kramdown rule that
  every tag must start at column 0 or the closing </div>s get swallowed into
  the paragraph above.

  The name is plain text; the e-mail address and each web page below it are the
  links. contact.web is a list, rendered one per line in the order given, so
  adding another page means adding a url/label pair in _data/positions.yml.
{% endcomment %}
{% assign c = site.data.positions.contact %}
<div class="member-grid">
<div class="member-card">
<div class="member-info">
<h4>Contact person</h4>
<div class="member-description">
<strong>{{ c.name }}</strong><br>
<a href="mailto:{{ c.email }}">{{ c.email }}</a>{% for w in c.web %}<br>
<a href="{{ w.url }}">{{ w.label | default: w.url }}</a>{% endfor %}
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
{{ c.name }}, {{ site.title }}<br>
{% for line in site.data.positions.postal.lines %}{{ line }}{% unless forloop.last %}<br>{% endunless %}
{% endfor %}</address>
</div>
</div>
</div>
</div>
