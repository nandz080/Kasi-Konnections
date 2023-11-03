from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route('/register', methods=['POST'])
    def register():
        # validation logic
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User(name=name, email=email, password=password)

        if not name or not email or not password:
            return render_template('register.html', error='All fields required')

        if User.query.filter_by(email=email).first():
            return render_template('register.html', error='Email already registered')

        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return redirect('/login')
        