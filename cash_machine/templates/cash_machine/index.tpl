{% extends 'atm/base.tpl' %}

{% block styles %}
    <link href="{{ static('cash_machine/keypad.css') }}" type="text/css" rel="stylesheet">
{% endblock %}


{% block content %}
<form method="post">
    {% csrf_token %}
    <div>
        {% include 'cash_machine/keypad.tpl' %}
    </div>
</form>
{% endblock%}

{% block scripts %}
    <script src="{{ static('cash_machine/keypad.js')}}"></script>
{% endblock %}