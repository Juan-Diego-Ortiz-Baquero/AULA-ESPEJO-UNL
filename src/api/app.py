import os
from flask import Flask, render_template

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/login/1', methods=['GET', 'POST'])
def login1():
    return render_template('login/login1.html')

#---LOGIN 2---

@app.route('/login/2', methods=['GET', 'POST'])
def login2():
    return render_template('login/login2.html')

#---LOGIN 3---

@app.route('/login/3', methods=['GET', 'POST'])
def login3():
    return render_template('login/login3.html')

#---LOGIN 4---

@app.route('/login/4', methods=['GET', 'POST'])
def login4():
    return render_template('login/login4.html')

#---MENU---
@app.route('/', methods=['GET'])
def home():
    return render_template('menu/home.html')

#---LOGIN SELECTOR---
@app.route('/login-selector', methods=['GET'])
def login_selector():
    return render_template('login/login-selector.html')


if __name__ == "__main__":
    app.run(debug=True)
