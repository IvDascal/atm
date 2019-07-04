<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %} | ATM</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link href="{{ static('cash_machine/css/main.css') }}" type="text/css" rel="stylesheet">

    {% block styles %}{% endblock %}

</head>
<body>
    <!--block for page top elements aka navigation bar-->
    <div class="page-header">
        {% block page_header %}{% endblock %}
    </div>

    <div class="container-fluid">
        <div class="page-content">
            {% block content %}{% endblock %}
        </div>
    </div>

    <div class="page-footer">
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    {% block scripts %} {% endblock %}
</body>
</html>
