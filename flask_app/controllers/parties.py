from crypt import methods
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.party import Party


@app.route('/new')
def new():
    if 'user_id' not in session:
        return redirect('/logout')

    data = {
        "id":session['user_id']
    }
    return render_template('new_party.html', instructors=User.get_instructors())

@app.route('/newparty', methods = ['POST'])
def newparty():
    if not Party.validate_party(request.form):
        return redirect('/new')
    if request.form['instructed']== "none":
        data = {
            "starttime": request.form["starttime"],
            "endtime": request.form["endtime"],
            "genre":int(request.form["genre"]),
        }
        Party.saved(data)
        return redirect('/dashboarda')
    else:
        data = {
            "starttime": request.form["starttime"],
            "endtime": request.form["endtime"],
            "genre":int(request.form["genre"]),
            "user_id": int(request.form["instructed"])
        }
        Party.save(data)
        return redirect('/dashboarda')

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    return render_template('edit_party.html', instructors=User.get_instructors(), party=Party.get_one(data))

@app.route('/editparty', methods = ['POST'])
def editparty():
    if not Party.validate_party(request.form):
        return redirect('/edit')
    elif request.form['instructed']== "none":
        data = {
            "starttime": request.form["starttime"],
            "endtime": request.form["endtime"],
            "genre":int(request.form["genre"]),
            "id":request.form["id"],
        }
        Party.updated(data)
        return redirect('/dashboarda')
    else:
        data = {
            "starttime": request.form["starttime"],
            "endtime": request.form["endtime"],
            "genre":int(request.form["genre"]),
            "user_id": int(request.form["instructed"]),
            "id":request.form["id"]
        }
        Party.update(data)
        return redirect('/dashboarda')

@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Party.delete(data)
    return redirect('/dashboarda')

@app.route('/needinstructor')
def needinstructor():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('needinstructor.html', user=User.get_by_id(data), parties=Party.get_upcoming())

@app.route('/needinstructori')
def needinstructori():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('needinstructori.html', user=User.get_by_id(data), parties=Party.get_upcoming())

@app.route('/take/<int:id>')
def take(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id,
        "user_id" : session['user_id']
    }
    Party.take(data)
    return redirect('/needinstructori')