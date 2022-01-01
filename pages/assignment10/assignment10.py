from flask import Blueprint, redirect, url_for,render_template
from flask import request, session
import mysql.connector
from datetime import date

assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/pages/assignment10',
    template_folder='templates'
)

# ------------- DATABASE CONNECTION --------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(
                         host="localhost",
                         user="root",
                         password="Y$11Gros"
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

@assignment10.route('/assignment10')
def search_func():
    query = "select * from users.user"
    query_reasult = interact_db(query, 'fetch')

    if request.method == 'POST':
        if 'y_id' in request.form:
          user_name = request.form['y_name']
          user_email= request.form['y_email']
          user_password = request.form['y_password']
          id = request.form['y_id']
          date_time = date.today()
          query = '''INSERT INTO `users`.`user` (`id`, `user_name`, `email`, `password`, `date`) VALUES('%s','%s', '%s','%s','%s');'''%(id,user_name, user_email,user_password,date_time)
          interact_db(query,'commit')
          query = "select * from users.user"
          query_reasult = interact_db(query, 'fetch')
        return render_template('welcome.html',users = query_reasult)

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
                  query = '''DELETE FROM `users`.`user` where id = ('%s') and user_name = ('%s');''' %(id, user_name)
                  interact_db(query, 'commit')
                  query = "select * from users.user"
                  query_reasult = interact_db(query, 'fetch')
                  return render_template('assignment10.html', id = id, user_name = user_name,users=query_reasult )
           return render_template('assignment10.html', users=query_reasult)

        if 'y_id_update' in request.args:
            query = "select * from users.user"
            query_reasult = interact_db(query, 'fetch')
            user_name = request.args['y_name_update']
            user_email = request.args['y_email_update']
            user_password = request.args['y_password_update']
            id = request.args['y_id_update']
            query_2 = "select COUNT(*) as exist from users.user WHERE users.user.id = ('%s');"%id
            query_reasult_2 = interact_db(query_2, 'fetch')
            for q in query_reasult_2:
                if q.exist == 1:
                    query = '''UPDATE `users`.`user` SET email = ('%s'),user_name = ('%s'),password = ('%s') WHERE id = (%s);''' %(user_email,user_name,user_password,id)
                    interact_db(query, 'commit')
                    query = "select * from users.user"
                    query_reasult = interact_db(query, 'fetch')
                    return render_template('assignment10.html', id=id, user=user_name,email = user_email,users=query_reasult)
            return render_template('assignment10.html', users=query_reasult)

    return render_template('assignment10.html',users = query_reasult)


@assignment10.route('/logout')
def logout():
    session.pop('username',None)
    session['logged_in'] = False
    return redirect(url_for('home_func'))
