from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from views.auth import auth_bp
from views.dashboard import dashboard_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()
    db.session.add(User(name='Kasi',email='<EMAIL>',password='<PASSWORD>'))
    db.session.commit()
    user = User.query.filter_by(email='<EMAIL>').first()
    print(user.check_password('<PASSWORD>'))
    print(User.query.all())
    print(User.query.filter_by(email='<EMAIL>').first())
    print(User.query.filter_by(email='<EMAIL>').first().check_password('<PASSWORD>'))
    
    """

@app.route('/')
def index():
    return 'hi'
"""
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method =='POST':
        #handle requests
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
        #handle requests
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['name'] = user.name
            session['email'] = user.email
            session['password'] = user.password
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid user')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if session['name']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html', user=user)
    
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')
"""

if __name__ == '__main__':
    app.run(debug=True)