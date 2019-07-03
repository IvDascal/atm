{% extends 'atm/base.tpl' %}

{% block styles %}
    <link href="{{ static('cash_machine/keypad.css') }}" type="text/css" rel="stylesheet">
{% endblock %}


{% block content %}
<form method="post">
    {% csrf_token %}

    <div class="form-group keypad">
        <label for="card_number">Card Number:</label>
        <input type="text" class="form-control card_num" id="card_number" name="card_number">
    </div>
    <div>
        {% include 'cash_machine/keypad.tpl' %}
    </div>
</form>
{% endblock%}

{% block scripts %}
    <script src="{{ static('cash_machine/card_num.js')}}"></script>
{% endblock %}