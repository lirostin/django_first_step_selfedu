<!DOCTYPE html>
<html>
<head>
         <meta charset="UTF-8">
         <title>{% block title %}{% endblock %}</title>
</head>
<body>
 
Часть из базового блока которая взялась с помощью параметра super 
{% block content %}
         {% block table_contents %}
         <ul>
         {% for li in list_table -%}
         <li>{{li}}</li>
         {% endfor -%}
         </ul>
         {% endblock table_contents %}
{% endblock %}
 
</body>
</html>