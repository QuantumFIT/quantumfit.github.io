---
permalink: /team/
layout: page
title: Team
description: "The people in the |QuantumFIT> research group."
comments: false
modified: 2026-09-02
breadcrumbs: true
---

<div class="group-section">
  <h2 class="group-section-title">Principal Investigator</h2>

  {% for member in site.data.group.principle_investigator %}
  <div class="pi-card">
    {% if member.image %}
    <div class="pi-photo">
      <img src="{{ site.url }}/{{ member.image }}" alt="{{ member.name }}">
    </div>
    {% endif %}
    <div class="pi-info">
      <h3>{{ member.name }}</h3>
      {% if member.facts %}
      {% comment %}
        markdownify wraps its output in <p>, which inside a <dd> adds a margin
        the grid gap already provides. Every value is a single line, so
        stripping the wrapper is safe here.
      {% endcomment %}
      <dl class="member-facts">
        {% for fact in member.facts %}
        <dt>{{ fact.label }}</dt>
        <dd>{{ fact.value | markdownify | replace: '<p>', '' | replace: '</p>', '' }}</dd>
        {% endfor %}
      </dl>
      {% endif %}
      {% if member.web %}
      <a class="pill-link" href="{{ member.web }}">{{ member.web_label | default: member.web }}</a>
      {% endif %}
    </div>
  </div>
  {% endfor %}
</div>

{% comment %}
  The three sections below render only when their list in _data/group.yml has
  entries, so a group with no BSc students (say) shows no empty BSc heading.
  The Principal Investigator section above is deliberately not guarded.

  A non-PI card is a name, a role tag and an e-mail address: the name links to
  the person's FIT BUT profile (`web` in _data/group.yml), which is where a bio
  belongs. Both the link and the address are optional, so a card degrades to
  just the name. Only the PI carries prose here.
{% endcomment %}
{% if site.data.group.phd_and_postdocs.size > 0 %}
<div class="group-section">
  <h2 class="group-section-title">PhD Students and Postdocs</h2>
  <div class="member-grid">
  {% for member in site.data.group.phd_and_postdocs %}
    <div class="member-card">
      <div class="member-info">
        <div class="member-heading">
          <h4>{% if member.web %}<a href="{{ member.web }}">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</h4>
          {% if member.role %}<span class="member-role">{{ member.role }}</span>{% endif %}
          {% if member.period %}<span class="member-period">{{ member.period }}</span>{% endif %}
        </div>
        {% if member.email %}<a class="member-email" href="mailto:{{ member.email }}">{{ member.email }}</a>{% endif %}
      </div>
    </div>
  {% endfor %}
  </div>
</div>
{% endif %}

{% if site.data.group.undergraduate_students.size > 0 %}
<div class="group-section">
  <h2 class="group-section-title">BSc/MSc Students</h2>
  <div class="member-grid">
  {% for member in site.data.group.undergraduate_students %}
    <div class="member-card">
      <div class="member-info">
        <div class="member-heading">
          <h4>{% if member.web %}<a href="{{ member.web }}">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</h4>
          {% if member.period %}<span class="member-period">{{ member.period }}</span>{% endif %}
        </div>
        {% if member.email %}<a class="member-email" href="mailto:{{ member.email }}">{{ member.email }}</a>{% endif %}
      </div>
    </div>
  {% endfor %}
  </div>
</div>
{% endif %}

{% if site.data.group.alumni.size > 0 %}
<div class="group-section">
  <h2 class="group-section-title">Alumni</h2>
  <div class="member-grid">
  {% for member in site.data.group.alumni %}
    <div class="member-card">
      <div class="member-info">
        <div class="member-heading">
          <h4>{% if member.web %}<a href="{{ member.web }}">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</h4>
          {% if member.period %}<span class="member-period">{{ member.period }}</span>{% endif %}
        </div>
        {% if member.email %}<a class="member-email" href="mailto:{{ member.email }}">{{ member.email }}</a>{% endif %}
      </div>
    </div>
  {% endfor %}
  </div>
</div>
{% endif %}
