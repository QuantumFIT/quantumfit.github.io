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

## Research

We work on **formal verification and efficient simulation of quantum circuits and
programs**. Quantum software is hard to get right and hard to test: the state space
grows exponentially with the number of qubits, and a quantum state cannot be
inspected without destroying it. Running a program and looking at the output --- the
usual way of finding bugs --- therefore does not get you very far.

Our approach is to describe whole *sets* of quantum states symbolically, using
automata, so that a property can be established for all of them at once instead of
one execution at a time. Current directions:

- **Automata-based verification and bug hunting in quantum circuits.** Sets of
  quantum states are represented as tree automata, which lets a circuit be checked
  against a pre-/post-condition specification without enumerating states. This is
  implemented in [AutoQ](https://github.com/fmlab-iis/AutoQ).
- **Level-synchronized tree automata**, a richer automata model that captures
  entanglement patterns which plain tree automata cannot express.
- **From circuits to programs**, extending the techniques to quantum programs with
  control flow, and to *parameterized* circuits --- a single proof that holds for
  every number of qubits, rather than one circuit size at a time.
- **Specification languages** practical enough that a property can be written down
  by hand and then checked automatically.
- **Faster simulation** through symbolic execution and loop summarization,
  implemented in [Medusa](https://github.com/s-jobra/MEDUSA/).

Much of this work is done with international collaborators, and appears at
programming-language and verification venues such as POPL, PLDI, CAV, TACAS and
ICCAD. See [Publications](/publications/) for the full list.

## Contact

{% for org in site.data.positions %}
**{{ org.title }}**{% if org.department %}, {{ org.department }}{% endif %}
{% if org.address %}{{ org.address }}{% endif %}{% if org.location %}, {{ org.location }}{% endif %}
{% if org.email %}Email: [{{ org.email }}](mailto:{{ org.email }}){% endif %}
{% endfor %}
