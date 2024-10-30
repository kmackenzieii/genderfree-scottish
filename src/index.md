---
layout: base.pug
eleventyImport:
  collections: 
    - events
    - faq
---

{% renderFile "./src/_includes/about.md" %}

{% for event in collections.events %}
{{ event.page.inputPath }}
{% endfor %}
{% assign today = site.time | date: "%s" %}
{% assign events = collections.events | sort: "start-time" %}
{% for class in collections.events %}
    {% assign class-start = class.start-time | date: "%s" %}
    {% if class-start >= today %}
        {% assign next-class = class %}
        {% break %}
    {% endif %}
    {% assign next-class = class %}
{% endfor %}
<div id="next">
<h2>{{next-class.start-time | date: "%A, %B %d"}}</h2>
{{next-class.start-time | date: "%l:%M %P"}} - {{next-class.end-time | date: "%l:%M %P"}}
<p>
<b>{{next-class.address}}</b>

</p>
<p>{{next-class.content}}.</p>

</div>

<div id="faq">
<h2>FAQ</h2>
{% for faq in collections.faq %}
<h3>{{ faq.question }}</h3>
<p>{{ faq.answer }}</p>
{% endfor %}
</div>

</div>