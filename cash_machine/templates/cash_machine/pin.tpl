{% extends 'atm/base.tpl' %}

{% block styles %}
    <link href="{{ static('cash_machine/keypad.css') }}" type="text/css" rel="stylesheet">
{% endblock %}

{% block content %}
<form method="post">
    {% csrf_token %}
    <div class="form-group keypad">
        <label for="pin">PIN:</label>
        <input type="password" class="form-control pin" id="pin" name="pin">
    </div>
    {% if error_msg %}
        <div class="keypad">
            <p>{{ error_msg }}</p>
        </div>
    {% endif %}
    <div>
        {% include 'cash_machine/keypad.tpl' %}
    </div>
</form>
{% endblock%}

{% block scripts %}
    <script src="{{ static('cash_machine/pin.js')}}"></script>
{% endblock %}