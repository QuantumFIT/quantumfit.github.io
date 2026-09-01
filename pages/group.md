---
permalink: /group/
layout: page
title: Group Members
description: "Group members: a list of current group members and alumni."
comments: false
modified: 2026-08-28
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
      {% comment %}Absolute URLs are used as-is; only site-relative paths get site.url.{% endcomment %}
      {% if member.bio_link contains "//" %}{% assign bio_href = member.bio_link %}{% else %}{% assign bio_href = site.url | append: member.bio_link %}{% endif %}
      <a href="{{ bio_href }}" class="member-link">View Biography</a>
      {% endif %}
    </div>
  </div>
  {% endfor %}
</div>

{% comment %}
  Each section below renders only when its list has entries, so a section that
  is not filled in yet stays hidden instead of showing a bare heading.
{% endcomment %}
{% if site.data.group.graduate_students.size > 0 %}
<div class="group-section">
  <h2 class="group-section-title">Ph.D. Students</h2>
  <div class="member-grid">
  {% for member in site.data.group.graduate_students %}
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
