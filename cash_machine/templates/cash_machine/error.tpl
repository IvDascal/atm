{% extends 'cash_machine/base.tpl' %}

{% block content %}

    <div>
        <h1 class="alert alert-danger">ОШИБКА:</h1>
        <p>{{ error.error_msg }}</p>
    </div>
    <a class="btn btn-warning" href="{{ error.error_back }}" role="button">Назад</a>

{% endblock%}