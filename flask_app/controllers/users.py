from crypt import methods
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.party import Party
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')      
def home():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    user = User.get_by_username (request.form)
    if not user:
        flash("Invalid Username")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash ("Incorrect Password")
        return redirect('/')
    session['user_id'] = user.id
    if user.level == 1:
        return redirect('/dashboarda')
    if user.level ==2:
        return redirect('/dashboardi')

@app.route('/register', methods = ['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/createuser')
    data = {
        "username": request.form["username"],
        "email": request.form["email"],
        "level":int(request.form["level"]),
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    id = User.save(data)
    session['user_id'] = id
    level = int(request.form["level"])
    if level == 1:
        return redirect('/dashboarda')
    else:
        return redirect('/dashboardi')

@app.route('/createuser')      
def createuser():
    return render_template('register.html')

@app.route('/dashboarda')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('dashboarda.html', user=User.get_by_id(data), parties=Party.get_upcoming())

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')

@app.route('/dashboardi')
def dashboardi():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('dashboardi.html', user=User.get_by_id(data), parties=Party.get_upcoming())
