# How do templates work
+ Templates contain the text of a response
+ With placeholder parts for the dynamic parts given by the specific `route`
+ This will be known by the context of the request
+ Match the template name with the function name
	+ if `def index()` -> `index.html`
	+ if `def landing(user)` -> landing.html
+ Template example for index.html:
```html
	<h1>Welome</h1>
```

+ Template example for landing.html
```html
	<h2>{{name}} has landed<h2>
```

+ *NB* Must import render_template from flask
+ To return the template response from a view function
	+ `return render_template('index.html')
	+ Template for the given view function
+ To return the dynamic parts:
	+ `return render_template('landing.html',name=name)`
	+ where the template placeholder `name` is assigned the name variable from the python script

# Jinja2 Variables
+ Jinja2 recognizes variables of many types
	+ {{myDict['key']}}
	+ {{myList[3]}}
	+ {{myList[index_var]}}
	+ {{myObj.method()}}
+ Variable can have filters seperated by |
+ Example: {{name|capitalize}}
+ Filters include:
	+ safe
	+ capitalize
	+ lower
	+ upper 
	+ title
	+ trim
	+ striptags
	+ And many more ...

# Template Conditionals
Example
```html
	
	{% if user %}
		<h1>Hello, {{user|capitalize}}<h1>
	{% else %}
		<h1>Hello, stranger</h1>
	{% endif %}
```
+ Similar for for loops
+ Template code that needs to be repeated can be included in another template
	+ `{% include 'innc.html' %}`

# Base Template
```html
	<html>
		<head>
			{% block head %}
			<title>{% block title %}{% endblock %} - My Application</title>
			{% endblock %}
		</head>
		<body>
			{% block body %}
			{% endblock %}
		</body>
	</html>

`
+ The `block` tags define elements that a **derived template** can change
+ A derived template:
```
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
	{{ super() }}
	<style>
	</style>
{% endblock %}
{% block body %}
<h1>Hello, World!</h1>
{% endblock %}
```
+ Content inbetween the tags will replace the placeholders in the base, but for the drived template
+ The use of `{{super}}` inside the derived template means that the derived template will just retain what is extended from the base template
+ **Base templates define blocks that can be overriden by derived templates**
