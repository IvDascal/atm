{% extends 'cash_machine/base.tpl' %}

{% block styles %}
    <link href="{{ static('cash_machine/css/keypad.css') }}" type="text/css" rel="stylesheet">
{% endblock %}


{% block content %}
<form method="post">
    {% csrf_token %}

    <div class="form-group keypad">
        <label for="card_number">Введите номер карты:</label>
        <input type="text" class="form-control card_num" id="card_number" name="card_number">
    </div>
    <div>
        {% include 'cash_machine/keypad.tpl' %}
    </div>
</form>
{% endblock%}

{% block scripts %}
    <script src="{{ static('cash_machine/js/card_num.js')}}"></script>
{% endblock %}