{% extends 'cash_machine/base.tpl' %}

{% block styles %}
    <link href="{{ static('cash_machine/css/transaction.css') }}" type="text/css" rel="stylesheet">
{% endblock %}

{% block content %}

    <div class="transaction">
        <a class="btn btn-primary btn-block btn-lg" href="balance" role="button">Баланс</a>
        <a class="btn btn-info btn-block btn-lg" href="withdraw" role="button">Снятие денег</a>
        <a class="btn btn-danger btn-block btn-lg" href="/" role="button">Выход</a>
    </div>

{% endblock%}