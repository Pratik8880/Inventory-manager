from flask import request, render_template, redirect, session, flash
from util.db_util import query_db

def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = query_db("SELECT * FROM users WHERE username = %s AND password = %s", (username, password), one=True)
        
        if user:
            session['user'] = user['username']
            return redirect('/inventory')
        else:
            flash('Invalid credentials')
    
    return render_template('login.html')

def logout_user():
    session.pop('user', None)
    return redirect('/login')
