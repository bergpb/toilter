# importando app do modulo app
from flask import render_template
from app import app

from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form_login = LoginForm()
    if form_login.validate_on_submit():
        print(form_login.username.data)
        print(form_login.password.data)
    else:
        print(form_login.errors)
        
    return render_template('login.html',
                           form=form_login)