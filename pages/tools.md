---
permalink: /tools/
layout: page
title: Tools
description: "Tools developed by the QuantumFIT research group."
comments: false
modified: 2026-09-01
breadcrumbs: true
---

## AutoQ

An automata-based verifier for quantum circuits and programs. Sets of quantum
states are represented as tree automata, which lets a circuit be checked against
a pre-/post-condition specification --- or searched for bugs --- without
enumerating individual states.

[github.com/fmlab-iis/AutoQ](https://github.com/fmlab-iis/AutoQ)

Introduced in
[AutoQ: An Automata-based Quantum Circuit Verifier](https://doi.org/10.1007/978-3-031-37709-9_7)
(CAV'23) and
[An Automata-based Framework for Verification and Bug Hunting in Quantum Circuits](https://doi.org/10.1145/3591270)
(PLDI'23), then extended with
[level-synchronized tree automata](https://doi.org/10.1145/3704868) (POPL'25),
[verification of quantum programs](https://doi.org/10.1007/978-3-031-90660-2_5)
(TACAS'25) and
[a practical specification language](https://doi.org/10.1007/978-3-032-32537-2_15)
(CAV'26).

## Medusa

A quantum circuit simulator that uses symbolic execution together with loop
summarization, so that a repeated block of gates is analysed once rather than
unrolled.

[github.com/s-jobra/MEDUSA](https://github.com/s-jobra/MEDUSA/)

Introduced in
[Accelerating Quantum Circuit Simulation with Symbolic Execution and Loop Summarization](https://doi.org/10.1145/3676536.3676711)
(ICCAD'24).
