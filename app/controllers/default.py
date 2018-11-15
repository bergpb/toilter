# importando app do modulo app
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, login

from app.models.tables import User
from app.models.forms import LoginForm


@login.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form_login = LoginForm()
    if form_login.validate_on_submit():
        user = User.query.filter_by(username=form_login.username.data).first()
        if user and user.password == form_login.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
        else:
            flash("Invalid login.")
    else:
        print(form_login.errors)
        
    return render_template('login.html',
                           form=form_login)
         
                  
@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("login"))
    
    
    