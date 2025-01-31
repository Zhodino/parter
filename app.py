from flask import Flask, render_template, redirect, url_for, flash
from sqlalchemy import null
from config import Config
from models.models import db, User
from forms import RegistrationForm, LoginForm, NothingForm
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import wtforms as wtf

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
bootstrap = Bootstrap(app)

polzovatel = null


@app.route('/', methods=['GET', 'POST'])
def index():
    global polzovatel
    form = RegistrationForm()
    login_form = LoginForm()
    nothing_form = NothingForm()
    oku = True
    oke = True

    if form.validate_on_submit():
        for i in User.query.all():
            if form.username.data == i.username:
                oku = False
            if form.email.data == i.email:
                oke = False
            if form.phone.data == i.phone:
                oke = False
        if oku and oke:
            print("ok")
            u = User(username=form.username.data, email=form.email.data, phone=form.phone.data, password_hash=form.password.data)
            db.session.add(u)
            db.session.commit()
            return render_template('index.html', login_form=login_form, form=nothing_form)
        elif oku and not oke:
            print("oku")
            flash("Email already taken")
            return render_template('index.html', login_form=login_form, form=form)
        elif oke and not oku:
            print("oke")
            flash("Username already taken")
            return render_template('index.html', login_form=login_form, form=form)
        elif not oke and not oku:
            print("not ok")
            flash("Username already taken")
            return render_template('index.html', login_form=login_form, form=form)

    if login_form.validate_on_submit():
        for i in User.query.all():
            if login_form.username.data == i.phone or login_form.username.data == i.email:
                if login_form.password.data == i.password_hash:

                    print("You have successfully logged in!")
                    polzovatel = i

                    return redirect(url_for('manage'))
                else:
                    flash("Incorrect password!")

    return render_template('index.html', login_form=login_form, form=form)


@app.route('/manage')
def manage():
    return render_template('manage.html')


@app.route('/logout')
def logout():
    global polzovatel
    polzovatel = null
    print("You have logged out!")
    return redirect("/")


@app.route('/add_user')
def add_user():
    new_user = User(username='john_doe', email='john@example.com', phone='+79169650904', password_hash='12345')
    db.session.add(new_user)
    db.session.commit()
    return 'User added!'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=5000)
