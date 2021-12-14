from flask import Flask, redirect, url_for,render_template
from flask import request
from flask import session

app = Flask(__name__)

# Home page
@app.route('/yuli')
@app.route('/')
def main_func():  # put application's code here
    # TODO
    return redirect(url_for('home_func'))

@app.route('/Home')
def home_func():
    return render_template('welcome.html')

# About me page
@app.route('/About_me')
def about_func():
    return render_template('cv.html')

# Pictures page
@app.route('/Pictures')
def pictures_func():
    return render_template('pictures.html')


# Pictures page
@app.route('/hobbies')
def hobbies_func():
    return render_template('assignment8.html',
                           hobbies = ['Basketball','Snowboard','Running','Reformer pilates','hiking','cooking','Freediving'])

# Contact page
@app.route('/contact')
def contact_func():
    if 'y_name' in request.args:
          name = request.args['y_name']
          email = request.args['y_email']
          password = request.args['y_password']
          return render_template('contact.html', user_name = name,user_email = email,user_password = password)
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)

