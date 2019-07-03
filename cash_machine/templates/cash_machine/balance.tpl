{% extends 'atm/base.tpl' %}

{% block content %}
    <div>
        <h1>Номер карты</h1>
        <p>{{ card.card_number }}</p>
        <h1>Сегодня</h1>
        <p>{{ today }}</p>
        <h1>Сумма на счету</h1>
        <p>{{ card.balance }}</p>

    </div>
    <div>
        <a class="btn btn-warning" href="transaction" role="button">Назад</a>
        <a class="btn btn-danger" href="/" role="button">Выход</a>
    </div>

{% endblock%}