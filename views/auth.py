#!/usr/bin/env python3
""""
a new user to the database - assuming add_user method is defined in User model
new_user.add_user()
# Redirect to login page
return redirect('/login')
app/views/auth.py
""" 
"""from flask import Blueprint, render_template, redirect, request, session
from app.models import User  # Assuming your User model is defined in app/models.py
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Validate and hash the password
        hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        new_user = User(name=name, email=email, password=hashed_password)
        # Add the user to the database (you need to define this method in models.py)
        new_user.save_to_db()


        return redirect('/login')

    return render_template('register.html')

    
    if not name or not email or not password:
        return render_template('register.html', error='All fields required')

    if User.query.filter_by(email=email).first():
        return render_template('register.html', error='Email already registered')
    
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
"""
from flask import Blueprint, render_template, redirect, request, session
from werkzeug.security import generate_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Validate email format using a regex
        email_regex = r'[^@]+@[^@]+\.[^@]+'
        if not re.match(email_regex, email):
            return render_template('register.html', error='Invalid email format')

        # Other validation logic
        if not name or not email or not password:
            return render_template('register.html', error='All fields required')

        if User.query.filter_by(email=email).first():
            return render_template('register.html', error='Email already registered')

        # Hash the password before storing
        hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        user = User(name=name, email=email, password=hashed_password)

        # Add the user to the database
        db.session.add(user)
        db.session.commit()

        return redirect('/login')

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')
