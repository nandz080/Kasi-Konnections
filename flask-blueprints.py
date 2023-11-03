# blueprints/auth.py
from flask import Blueprint 

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
  # login logic
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

# blueprints/dashboard.py 
from flask import Blueprint

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard') 
def dashboard():
  # dashboard logic
    if session['name']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html', user=user)
    
    return redirect('/login')

# app.py
from blueprints.auth import auth_bp 
from blueprints.dashboard import dashboard_bp

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)



####33 Add validation logic when creating new users.
@app.route('/register', methods=['POST']) 
def register():

  # Validate name, email, password
  if not valid_name(name):
    return error

  if not valid_email(email):
    return error
    
  # Create user


  #######33 Use Flask-WTF for form validation and CSRF protection
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class RegistrationForm(FlaskForm):
  name = StringField('Name', validators=[InputRequired()])
  email = StringField('Email', validators=[InputRequired(), Email()])
  password = PasswordField('Password', validators=[InputRequired()]) 

@app.route('/register', methods=['GET', 'POST'])
def register():

  form = RegistrationForm()

  if form.validate_on_submit():
    # Create user
  else:
    return render_template('register.html', form=form)



########## Use Flask-SQLAlchemy pagination when querying users
@app.route('/users')
def users():
  page = request.args.get('page', 1, type=int)
  users = User.query.paginate(page=page, per_page=10) 
  return render_template('users.html', users=users)




###########33 Add logging to record events and errors
import logging 
logger = logging.getLogger(__name__)

@app.route('/register', methods=['POST'])
def register():
  try: 
    # Create user
  except Exception as e:
    logger.error("Error creating user: %s", e)
    return error
