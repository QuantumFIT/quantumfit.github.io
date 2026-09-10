---
permalink: /about/
layout: page
title: About |QuantumFIT⟩
description: A brief introduction to the |QuantumFIT⟩ research group and this website.
comments: false
modified: 2026-09-10
breadcrumbs: true
---

{% comment %}
  The pipe is escaped. Unescaped, kramdown reads it as a table cell separator
  and turns this paragraph into a one-row table, cells "**" and the rest --
  which is exactly what it did until this comment was written. Anywhere the
  group's name appears in markdown body text it needs the backslash; front
  matter, raw HTML and Liquid output outside markdown are unaffected.
{% endcomment %}
**\|QuantumFIT⟩** is a research group at the [Faculty of Information Technology](https://www.fit.vut.cz/), [Brno University of Technology](https://www.vut.cz/), bringing together researchers and students interested in studying quantum computing systems in the broad sense. The main aim of the group is empowering the transition from today's noisy, small-scale quantum devices towards machines delivering a practical quantum advantage --- by developing the algorithmic foundations and the software tools needed to design, analyse, and trust quantum computation.

The group builds on a strong background in formal methods, automated reasoning, and automata theory, and transfers these techniques into the quantum domain: symbolic and decision-diagram-based representations of quantum states and operations, SAT/SMT solving, and rigorous semantics of quantum circuits and programs. On top of these foundations we develop [prototype tools]({{ site.url }}/tools/) --- simulators, optimizers, verifiers, synthesis engines, and tools supporting the design of quantum error-correcting codes --- and evaluate them on realistic benchmarks. The same foundations also let us go beyond analysing existing computations and design new ones: quantum algorithms and trusted building blocks --- quantum arithmetic, oracles, state-preparation and uncomputation primitives --- that come with correctness guarantees and a known resource cost, and can therefore be reused as reliable components of larger quantum computations. Besides basic research, the group is involved in building the surrounding community infrastructure, such as benchmark collections for the evaluation of such tools.

## Research Focus

{% comment %}
  The lead phrase of each item is bold so the list can be skimmed for a
  subject rather than read straight through; the rest of the item is the
  same sentence it was written as.

  Internal links go through {{ site.url }}, not a bare /tools/. A
  root-relative link jumps out of the /preview/ build straight to the live
  site -- which is what the two links this page used to carry did.
{% endcomment %}
Analysis, verification, optimization, and synthesis of quantum circuits and programs, together with the underlying methods from automated reasoning, automata theory, and logic, including:

* **Simulation of quantum circuits and programs** --- scalable symbolic and semi-symbolic simulation techniques based on decision diagrams, targeting both near-term (NISQ) and fault-tolerant workloads.
* **Verification and equivalence checking** --- automated reasoning about the equivalence of quantum circuits, their correctness with respect to a specification, and properties of quantum programs, using decision procedures, model checking, and automata-based representations of sets of quantum states.
* **Optimization and compilation** --- reducing the resource cost of quantum computation (gate count, T-count and T-depth, circuit depth, number of qubits, ancilla usage), fault-tolerant compilation and resource estimation, and hardware-aware mapping and routing onto real devices.
* **Synthesis of quantum circuits** --- exact and approximate synthesis driven by solvers (SAT, SMT, #SAT, QBF) and by search, including synthesis over restricted and hardware-native gate sets, and probabilistic constructions such as repeat-until-success circuits.
* **Quantum algorithms and trusted building blocks** --- design of new quantum algorithms and of reusable, resource-efficient circuit primitives (quantum arithmetic, oracles, multi-controlled operations, state preparation, measurement-based uncomputation) whose correctness and cost are established rigorously, so that they can serve as trusted components of larger computations.
* **Quantum error correction** --- techniques and tools supporting the design, analysis, and evaluation of quantum error-correcting codes and their decoders, and the assessment of the overhead they impose on fault-tolerant execution.
* **Benchmarks and community infrastructure** --- benchmark suites, input/output formats, and competitions of tools for automated reasoning over quantum circuits, enabling a fair and reproducible comparison of the approaches developed in the field.

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
