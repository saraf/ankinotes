---
layout: tags
title: Browse by Tag Group
permalink: /tags/
---

# 🏷 Browse Notes by Topic

{% assign tag_groups = site.data.tag_groups %}
{% for group in tag_groups %}
## {{ group[0] }}

{% for tag in group[1] %}
- [{{ tag }}]({{ site.baseurl }}/tags/{{ tag | slugify }}/)
{% endfor %}

{% endfor %}
