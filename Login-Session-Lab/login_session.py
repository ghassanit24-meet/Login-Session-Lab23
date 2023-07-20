from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', ) # What methods are needed?
def home():
	return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', ) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')
@app.route('/submit_quote' , methods=['GET', 'POST'])
def method():
	if request.method == 'POST':
		age = request.form.get('age')
		login_session['age'] = age

		return redirect(url_for('error.html'))
	return render_template('home.html')	
@app.route('/error.html')
def error():
	age = login_session.get('age', 'N/A')
	return render_template('error.html')

if __name__ == '__main__':
	app.run(debug=True)When the form is submitted, store the form's information in login_session, example: login_session['age'] = age.