from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models import Users
from flask_login import login_user, logout_user


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            flash("Такой пользователь уже существует", "danger")
            return redirect(url_for('register'))

        # создание нового пользователя
        new_user = Users(email=email, name=name, password=password)
        new_user.hashPassword(password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('my'))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()

        if user and user.checkPassword(password):
            login_user(user)
            return redirect(url_for('my'))
        else:
            flash("Неверные учетные данные", "danger")

    return render_template("login.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))