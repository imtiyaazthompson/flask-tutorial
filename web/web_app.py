from flask import Flask,request,g,current_app,session,make_response,redirect,render_template

app = Flask(__name__)

# Map URL to Python functions with routes

# Root URL
@app.route('/')
def index():
	return render_template('index.html')


# Dynamic URL - <string> or <type:var>
@app.route('/landing/<user>')
def landing(user):
	#if user == 'admin': return '<p>Unauthorized!</p>', 400
	users.append(user)
	return render_template('landing.html',name=user)


# Testing template for loops
@app.route('/users')
def users():
	return render_template('list.html',users=users)

# Certain objects, like request (encapsulates user request data)
# Are only available in certain contexts
# Namely application and request contexts
# The object will then act like a global variable
@app.route('/browser')
def get_browser():
	# Defualt, currently in request context
	ua = request.headers.get('User-Agent')
	return '<p>Web viewed through {}</p>'.format(ua)


# To handle responses, better to encapusulate them
# into respone objects, on which methods can be called
@app.route('/responses/<text>')
def response_encap(text):
	resp = make_response('<h3>{}</h3>'.format(text))
	resp.set_cookie('answer','42')
	return resp


# URL redirects, useful in html forms
@app.route('/home')
def redir():
	return redirect('http://www.google.com')

# From application context: g, current_app
# from request context: request, session
def context_switch(context='request'):
	if context == 'request': # push request context
		ctx = app.request_context()
		ctx.push()
		return ctx
	elif context == 'application':
		ctx = app.app_context()
		ctx.push()
		return ctx
	
# Pop the context from the stack
def pop_context(context):
	context.pop()

# Run the server
if __name__ == '__main__':
	# Put your variables here
	users = []
	app.run(debug=True)
