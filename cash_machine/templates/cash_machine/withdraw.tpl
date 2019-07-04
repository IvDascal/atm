{% extends 'cash_machine/base.tpl' %}

{% block styles %}
    <link href="{{ static('cash_machine/css/keypad.css') }}" type="text/css" rel="stylesheet">
{% endblock %}

{% block content %}
<form method="post">
    {% csrf_token %}

    <div class="form-group keypad">
        <label for="amount">Введите сумму:</label>
        <input type="text" class="form-control amount" id="amount" name="amount">
    </div>

    <div>
        {% include 'cash_machine/keypad.tpl' %}
    </div>
</form>
{% endblock%}

{% block scripts %}
    <script src="{{ static('cash_machine/js/withdraw.js')}}"></script>
{% endblock %}