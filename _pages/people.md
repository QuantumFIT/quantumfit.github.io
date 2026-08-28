---
permalink: /people/
title: "People"
author_profile: false
---

{% for person in site.data.team %}
## {{ person.name }}
{{ person.role }}

{% if person.bio %}{{ person.bio }}{% endif %}
{% if person.email %}[{{ person.email }}](mailto:{{ person.email }}){% endif %}{% if person.website %} &middot; [website]({{ person.website }}){% endif %}

---
{% endfor %}

<!-- Group members live in _data/team.yml -- add one entry per person there. -->
