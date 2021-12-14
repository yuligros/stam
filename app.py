from flask import Flask, redirect, url_for,render_template
from flask import request
from flask import session

app = Flask(__name__)

# Home page
@app.route('/yuli')
@app.route('/')
def main_func():  # put application's code here
    # TODO
    return redirect(url_for('home'))

@app.route('/Home')
def home_func():
    return render_template('welcome.html')

# About me page
@app.route('/About me')
def about_func():
    return render_template('cv.html')

# Pictures page
@app.route('/Pictures')
def pictures_func():
    return render_template('pictures.html')

# Contact page
@app.route('/contact')
def contact_func():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)

