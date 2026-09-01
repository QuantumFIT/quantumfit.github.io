---
permalink: /team/
layout: page
title: Team
description: "The people in the QuantumFIT research group."
comments: false
modified: 2026-09-01
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
      <div class="member-bio">{{ member.bio | markdownify }}</div>
      {% if member.bio_link %}
      <a href="{{ site.url }}{{ member.bio_link }}" class="member-link">View Biography</a>
      {% endif %}
    </div>
  </div>
  {% endfor %}
</div>

{% comment %}
  The three sections below render only when their list in _data/group.yml has
  entries, so a group with no BSc students (say) shows no empty BSc heading.
  The Principal Investigator section above is deliberately not guarded.
{% endcomment %}
{% if site.data.group.phd_and_postdocs.size > 0 %}
<div class="group-section">
  <h2 class="group-section-title">Ph.D. Students and Postdocs</h2>
  <div class="member-grid">
  {% for member in site.data.group.phd_and_postdocs %}
    <div class="member-card">
      <div class="member-info">
        <h4>{{ member.name }}</h4>
        {% if member.role %}<span class="member-role">{{ member.role }}</span>{% endif %}
        {% if member.period %}<span class="member-period">{{ member.period }}</span>{% endif %}
        <div class="member-description">{{ member.description | markdownify }}</div>
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
        <h4>{{ member.name }}</h4>
        {% if member.period %}<span class="member-period">{{ member.period }}</span>{% endif %}
        <div class="member-description">{{ member.description | markdownify }}</div>
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
        <h4>{{ member.name }}</h4>
        {% if member.period %}<span class="member-period">{{ member.period }}</span>{% endif %}
        <div class="member-description">{{ member.description | markdownify }}</div>
      </div>
    </div>
  {% endfor %}
  </div>
</div>
{% endif %}
