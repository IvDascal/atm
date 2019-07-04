{% extends 'atm/base.tpl' %}

{% block content %}
    <div>
        <h1>Номер карты</h1>
        <p>{{ transaction.card.card_number }}</p>
        <h1>Дата</h1>
        <p>{{ transaction.created }}</p>
        <h1>Снятая сумма</h1>
        <p>{{ transaction.withdraw_amount }}</p>
        <h1>Остаток на счету</h1>
        <p>{{ transaction.card.balance }}</p>

    </div>
    <div>
        <a class="btn btn-warning" href="transaction" role="button">Назад</a>
        <a class="btn btn-danger" href="/" role="button">Выход</a>
    </div>

{% endblock%}