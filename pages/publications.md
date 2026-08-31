---
permalink: /publications/
layout: page
title: Publications
description: "Publications of the QuantumFIT research group."
comments: false
modified: 2026-08-31
breadcrumbs: true
---

<!--
  Render each entry's sub-list (preliminary version, technical report, slides,
  tool, artifact, video, ...) as a row of pill-shaped tags instead of a vertical
  bullet list, matching https://ondrik.github.io/publications/ . The markdown
  below keeps the plain nested lists; only the CSS changes how they look.

  The CSS is inline here rather than in a local _sass/ file for the same reason
  as the hero background in _layouts/home.html: the theme is pulled in via
  remote_theme, and its own sass files @import each other by bare name, so a
  local _sass/ copy is not reliably picked up. A <style> block in the page body
  is page-local, needs no theme internals, and cannot be shadowed.

  Selectors target `.entry-content li ul`, the structure the theme actually
  emits for a nested markdown list (verified against the rendered page).
-->
<style>
  .entry-content li ul {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5em 0.6em;
    list-style: none;
    margin: 0.6em 0 1.1em;
    padding-left: 0;
  }

  .entry-content li ul li {
    margin-bottom: 0;
    padding: 0.15em 0.8em;
    border: 1px solid rgba(44, 129, 186, 0.4);
    border-radius: 999px;
    font-size: 0.85em;
    line-height: 1.7;
  }

  /* The theme gives every link inside an <li> a dotted bottom border that
     turns solid on hover; inside a pill that reads as a stray underline. */
  .entry-content li ul li a,
  .entry-content li ul li a:hover {
    border-bottom: none;
  }

  .entry-content li ul li:hover {
    border-color: #2c81ba;
    background-color: #f1f8ff;
  }
</style>

## 2026

* W. Tsai, Y. Chen, and O. Lengal.
[A Practical Specification Language for Automatic Quantum Program Verification](https://doi.org/10.1007/978-3-032-32537-2_15).
In *Proc. of 38th International Conference on Computer Aided Verification* --- [CAV'26](https://conferences.i-cav.org/2026/),
Lisboa, Portugal,
volume 16684 of LNCS,
pages 302--325, 2026.
Springer-Verlag.
  * 📄 [preliminary version](https://github.com/ondrik/ondrik.github.io/raw/master/publications/cav26-quantum-specification.pdf)
  * 📝 [technical report](https://arxiv.org/abs/2605.05786)
  * 📊 [slides](https://github.com/ondrik/ondrik.github.io/raw/master/presentations/cav26-autoq-specification.pdf)
  * 🛠️ [AutoQ](https://github.com/fmlab-iis/AutoQ)
  * 📦 [artifact](https://doi.org/10.5281/zenodo.19756802)

* P. A. Abdulla, Y. Chen, M. Hecko, L. Holik, O. Lengal, J. Lin, and R. S. Thinniyam.
[Parameterized Verification of Quantum Circuits](https://doi.org/10.1145/3776712).
In *Proc. of 53rd ACM SIGPLAN Symposium on Principles of Programming Languages* --- [POPL'26](https://popl26.sigplan.org/), PACMPL 10 (POPL),
Rennes, France,
article 70, pages 2021--2050, 2026.
ACM.
  * 📄 [preliminary version](https://github.com/ondrik/ondrik.github.io/raw/master/publications/popl26-swtas-for-quantum.pdf)
  * 📊 [slides](https://github.com/ondrik/ondrik.github.io/raw/master/presentations/popl26-quantum-swta.pdf)
  * 🎥 [video](https://www.youtube.com/watch?v=JUsI21KtXG4)
  * 🎥 [video](https://www.youtube.com/watch?v=-o0lX1CfMz0) from a relevant [FLAT talk](https://flat.fc.up.pt/)

## 2025

* Y. Chen, K. Chung, O. Lengal, J. Lin, W. Tsai, and D. Yen.
[An Automata-Based Framework for Verification and Bug Hunting in Quantum Circuits](https://doi.org/10.1145/3725728).
Communications of the ACM (CACM) 68(6), pages 85--93, 2025.

* Y. Chen, K. Chung, M. Hsieh, W. Huang, O. Lengal, J.Lin, and W. Tsai.
[AutoQ 2.0: From Verification of Quantum Circuits to Verification of Quantum Programs](https://doi.org/10.1007/978-3-031-90660-2_5).
In *Proc. of 31th International Conference on Tools and Algorithms for the Construction and Analysis of Systems* --- [TACAS'25](https://etaps.org/2025/conferences/tacas/),
Hamilton, Canada,
volume 15698 of LNCS,
pages 87--108, 2025.
Springer-Verlag.
  * 📄 [preliminary version](https://github.com/ondrik/ondrik.github.io/raw/master/publications/tacas25-autoq-2-programs.pdf)
  * 📝 [technical report](https://arxiv.org/abs/2411.09121)
  * 🛠️ [AutoQ](https://github.com/fmlab-iis/AutoQ)
  * 📦 [artifact](https://doi.org/10.5281/zenodo.14114791)
  * 📊 [slides](https://github.com/ondrik/ondrik.github.io/raw/master/presentations/tacas25-autoq-2-programs.pdf) ([.pptx](https://github.com/ondrik/ondrik.github.io/raw/master/presentations/tacas25-autoq-2-programs.pptx))

* P. A. Abdulla, Y. Chen, Y. Chen, L. Holik, O. Lengal, J. Lin, F. Lo, and W. Tsai.
[Verifying Quantum Circuits with Level-Synchronized Tree Automata](https://doi.org/10.1145/3704868).
In *Proc. of 52nd ACM SIGPLAN Symposium on Principles of Programming Languages* --- [POPL'25](https://popl25.sigplan.org/), PACMPL 9 (POPL),
Denver, Colorado, USA,
article 32, pages 923--953, 2025.
ACM.
  * 📄 [preliminary version](https://github.com/ondrik/ondrik.github.io/raw/master/publications/popl25-lstas-for-quantum.pdf)
  * 📝 [technical report](https://arxiv.org/abs/2410.18540)
  * 📦 [artifact](https://doi.org/10.5281/zenodo.13957472)
  * 🛠️ [AutoQ](https://github.com/alan23273850/AutoQ/)
  * 📊 [slides](https://github.com/ondrik/ondrik.github.io/raw/master/presentations/vqc25-automata-quantum.pdf) (from a [VQC'25](https://verifiedqc.github.io/2025/))
  * 🖼️ [poster](https://github.com/ondrik/ondrik.github.io/raw/master/presentations/vqc25-poster-autoq.pdf)

## 2024

* T. Chen, Y. Chen, J. Jiang, S. Jobranova, and O. Lengal.
[Accelerating Quantum Circuit Simulation with Symbolic Execution and Loop Summarization](https://doi.org/10.1145/3676536.3676711).
In *Proc. of 2024 ACM/IEEE International Conference on Computer-Aided Design* --- [ICCAD'24](https://2024.iccad.com/),
New Jersey, USA,
Article No. 42,
pages 1--9, 2024.
ACM.
  * 📄 [preliminary version](https://github.com/ondrik/ondrik.github.io/raw/master/publications/iccad24-quantum-symb-exec.pdf)
  * 📊 [slides](https://github.com/ondrik/ondrik.github.io/raw/master/presentations/iccad24-quantum-symbolic-exec.pdf)
  * 🛠️ [Medusa](https://github.com/s-jobra/MEDUSA/)
  * 📦 [artifact](https://doi.org/10.5281/zenodo.13243595)

## 2023

* Y. Chen, K. Chung, O. Lengal, J. Lin, and W. Tsai.
[AutoQ: An Automata-based Quantum Circuit Verifier](https://doi.org/10.1007/978-3-031-37709-9_7).
In *Proc. of 35th International Conference on Computer Aided Verification* --- [CAV'23](http://www.i-cav.org/2023),
Paris, France,
volume 13966 of LNCS,
pages 139--153, 2023.
Springer-Verlag.
  * 📄 [preliminary version](https://github.com/ondrik/ondrik.github.io/raw/master/publications/cav23-autoq.pdf)
  * 📦 [artifact](https://doi.org/10.5281/zenodo.7966542)
  * 🛠️ [AutoQ](https://github.com/alan23273850/AutoQ/)

* Y. Chen, K. Chung, O. Lengal, J. Lin, W. Tsai, and D. Yen.
[An Automata-based Framework for Verification and Bug Hunting in Quantum Circuits](https://doi.org/10.1145/3591270).
In *Proc. of 44th ACM SIGPLAN Conference on Programming Language Design and Implementation* --- [PLDI'23](https://pldi23.sigplan.org/), PACMPL 7 (PLDI),
Orlando, Florida, USA,
article 156, pages 1218--1243, 2023.
ACM.
  * 📄 [preliminary version](https://github.com/ondrik/ondrik.github.io/raw/master/publications/pldi23-quantum-bug-hunting.pdf)
  * 📝 [technical report](https://arxiv.org/abs/2301.07747)
  * 📦 [artifact](https://doi.org/10.5281/zenodo.7707349)
  * 🎥 [video](https://www.youtube.com/live/1L1eKWwa6fE?t=4481)
  * 📊 [slides](https://github.com/ondrik/ondrik.github.io/raw/master/presentations/pldi23-quantum-bug-hunting.pdf) ([.pptx](https://github.com/ondrik/ondrik.github.io/raw/master/presentations/pldi23-quantum-bug-hunting.pptx))
  * 🛠️ [AutoQ](https://github.com/alan23273850/AutoQ/)
  * 🏆 **Distinguished Paper of PLDI'23**
