from flask import Flask, redirect, url_for,render_template
from flask import request, session
import mysql.connector


app = Flask(__name__)
app.secret_key = '123'
app.permanent_session_lifetime = 15


# Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Y$11Gros"
)

# Print success connection
print(mydb)

if __name__ == '__main__':
    app.run(debug=True)


# Home page
@app.route('/yuli')
@app.route('/')
def main_func():  # put application's code here
    # TODO
    return redirect(url_for('home_func'))

@app.route('/Home')
def home_func():
    session['user_name'] = 'Stranger'
    return render_template('welcome.html')

# About me page
@app.route('/About_me')
def about_func():
    return render_template('cv.html')


# Hobbies page
@app.route('/hobbies')
def hobbies_func():
    return render_template('assignment8.html',
                           hobbies = ['Basketball','Snowboard','Running','Reformer pilates','hiking','cooking','Free - diving'])

# Contact page
@app.route('/contact')
def contact_func():
    if 'y_name' in request.args:
          name = request.args['y_name']
          email = request.args['y_email']
          password = request.args['y_password']
          return render_template('contact.html', user_name = name,user_email = email,user_password = password)
    return render_template('contact.html')

# Contact page
@app.route('/Search',methods = ['GET','POST'])
def search_func():
    user_name,second_name = '',''
    users = get_users()
    if_exist = False

    if request.method == 'POST':
          user_name = request.form['y_name']
          user_email= request.form['y_email']
          user_password = request.form['y_password']
          session['user_name'] = user_name
          session['logged_in'] = True
          return render_template('welcome.html',
                                 user_name=user_name)

    if request.method == 'GET':
      if 'y_name' in request.args:
           user_name = request.args['y_name']
           email = request.args['y_email']
           session['user_name'] = user_name
           session['logged_in'] = True
           if_exist = check_if_user_exist(user_name,users)
           return render_template('assignment9.html',
                                  user_name=user_name,
                                  email = email,
                                  is_exist = if_exist)

      else:
          return render_template('assignment9.html',
                                 users=users,is_exist = if_exist)

    return render_template('assignment9.html')



def get_users():
    users = {'user1': {'user_name': 'yuli', 'email' : 'yuli11@gmail.com'},
             'user2': {'user_name': 'yosik', 'email': 'yosik12@gmail.com'},
             'user3': {'user_name': 'erez', 'email': 'erezMaster@gmail.com'},
             'user4': {'user_name': 'amit', 'email': 'tuli@gmail.com'},
             'user5': {'user_name': 'guy', 'email': 'guyTheKing@gmail.com'},
             'user6': {'user_name': 'shahaf', 'email': 'shahafgros@gmail.com'},
             'user7': {'user_name': 'dor', 'email': 'dori100@gmail.com'},
             'user8': {'user_name': 'itamar', 'email': 'itamari@gmail.com'}}
    return users


def check_if_user_exist(user,users):
    for id, values in users.items():
        for key in values:
            if values[key] == user:
                return True;
    return False











