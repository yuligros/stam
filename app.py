from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)



#Thid decorator must to be the closest to the function
@app.route('/home')
@app.route('/')
def hello_world():  # put application's code here
    # TODO
    return redirect(url_for('about'))

@app.route('/home_page', methods = ['Get'])
def home():  # put application's code here
    found = True

    if found:
        name = 'yuli'
        return render_template('index.html', name=name, color='green')
    else:
        return render_template('index.html')

@app.route('/catalog', methods = ['Get'])
def catalog():  # put application's code here
    return render_template('catalog.html')

@app.route('/about', methods = ['Get'])
def about():  # put application's code here
    return render_template('about.html', uni='BGU',
                           profiles={'names':'yuli','second':'grossman'},
                           degrees=['BSc','Btchlor'])


if __name__ == '__main__':
    app.run(debug=True)

