{% extends 'atm/base.tpl' %}

{% block styles %}
    <link href="{{ static('cash_machine/keypad.css') }}" type="text/css" rel="stylesheet">
{% endblock %}

{% block content %}
<form method="post">
    {% csrf_tokent %}

    <div class="form-group keypad">
        <label for="card_number">Card Number:</label>
        <input type="text" class="form-control" id="card_number">
    </div>
    <div>
        <table class="keypad">
            <tr class="key-row">
                <td class="key-cell">
                    <button class="btn btn-outline-dark key" type="button">7</button>
                </td>
                <td class="key-cell">
                    <button class="btn btn-outline-dark key" type="button">8</button>
                </td>
                <td class="key-cell">
                    <button class="btn btn-outline-dark key" type="button">9</button>
                </td>

            </tr>
            <tr class="key-row">
                <td class="key-cell">
                    <button class="btn btn-outline-dark key" type="button">4</button>
                </td>
                <td class="key-cell">
                    <button class="btn btn-outline-dark key" type="button">5</button>
                </td>
                <td class="key-cell">
                    <button class="btn btn-outline-dark key" type="button">6</button>
                </td>
            </tr>
            <tr class="key-row">
                <td class="key-cell">
                    <button class="btn btn-outline-dark key" type="button">1</button>
                </td>
                <td class="key-cell">
                    <button class="btn btn-outline-dark key" type="button">2</button>
                </td>
                <td class="key-cell">
                    <button class="btn btn-outline-dark key" type="button">3</button>
                </td>

            </tr>
            <tr class="key-row">
                <td class="key-cell">
                    <button class="btn btn-outline-success key" type="submit">OK</button>
                </td>
                <td class="key-cell">
                    <button class="btn btn-outline-dark key" type="button">0</button>
                </td>
                <td class="key-cell">
                    <button class="btn btn-outline-danger key" type="button">Очистить</button>
                </td>
            </tr>
        </table>
    </div>
</form>
{% endblock%}