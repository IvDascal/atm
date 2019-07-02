{% extends 'atm/base.tpl' %}



{% block content %}
<form method="post">
    {% csrf_token %}
    <div>
        {% include 'cash_machine/keypad.tpl' %}
    </div>
</form>
{% endblock%}