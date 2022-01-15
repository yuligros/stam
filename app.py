from flask import Flask, redirect, url_for, render_template, jsonify
from flask import request, session
import mysql.connector
import mysql.connector
from datetime import date
import requests
import random

app = Flask(__name__)
app.secret_key = '123'
app.permanent_session_lifetime = 30


# import assignment 10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


# ------------- DATABASE CONNECTION --------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(
                         host="localhost",
                         user="root",
                         password="root",
                         database='users'
    )


    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value
# ------------------------------------------------- #


@app.route('/users')
def func_users():
    query = "select * from users.user"
    query_reasult = interact_db(query, 'fetch')
    return render_template('users.html', users = query_reasult)

# @app.route('/delete_user')
# def func_delete_user():
#     return render_template('users.html')

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
@app.route('/Search',methods = ['GET','POST'])
def search_func():

    if request.method == 'POST':
          user_name = request.form['y_name']
          user_email= request.form['y_email']
          user_password = request.form['y_password']
          id = request.form['y_id']
          date_time = date.today()
          session['user_name'] = user_name
          session['logged_in'] = True
          query = '''INSERT INTO `users`.`user` (`id`, `user_name`, `email`, `password`, `date`) VALUES('%s','%s', '%s','%s','%s');'''%(id,user_name, user_email,user_password,date_time)
          interact_db(query,'commit')
          return render_template('welcome.html')

    if request.method == 'GET':
        query = "select * from users.user"
        query_reasult = interact_db(query, 'fetch')
        if 'y_id' in request.args:
           id = request.args['y_id']
           user_name = request.args['y_name']
           query_2 = "select COUNT(*) as exist from users.user WHERE users.user.id = ('%s');"%id
           query_reasult_2 = interact_db(query_2, 'fetch')
           for q in query_reasult_2:
              if q.exist == 1:
                session['user_name'] = user_name
                session['logged_in'] = True
                return render_template('assignment9.html', id = id, user_name = user_name)
           return render_template('users.html', users=query_reasult)

    return render_template('assignment9.html')


@app.route('/logout')
def logout():
    session.pop('username',None)
    session['logged_in'] = False
    return redirect(url_for('home_func'))



#users to a json file
@app.route('/assignment11/users')
def func_json():
    query = "select * from users.user"
    query_reasult = interact_db(query, 'fetch')
    return jsonify(query_reasult)



@app.route('/assignment11/outer_source',methods = ['GET'])
def req_backend_func():
    users = []
    if 'user_id' in request.args:
        user_id = int(request.args['user_id'])
        res = requests.get(f'https://reqres.in/api/users/{user_id}')
        res = res.json()
        users.append(res)
        return  render_template('assignment11.html',users = users)

    if 'user_id_front' in request.args:
        user_id_front = int(request.args['user_id_front'])
        return  render_template('assignment11.html',user_id_front = user_id_front)

    return render_template('assignment11.html')


#Assignment_12
@app.route('/assignment12/restapi_users/',defaults = {'USER_ID': None})
@app.route('/assignment12/restapi_users/<int:USER_ID>')
def get_id(USER_ID = None):
    if USER_ID:
        print(type(USER_ID))
        query = "select * from users.user WHERE users.user.id = ('%s');"%USER_ID
        query_reasult = interact_db(query, 'fetch')
        if(query_reasult):
             return jsonify(query_reasult)
        else:
            return jsonify(
        {
            'Error': 'We are sorry, but the user does not exist'
        })

    return jsonify(
        {
            'Error': 'We are sorry, but you did not insert the user ID '
        }
    )



if __name__ == '__main__':
    app.run(debug=True)








