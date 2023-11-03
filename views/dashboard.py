from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if session.get('user'):
     user = User.query.filter_by(id=session['user']['id']).first()
     orders = Order.query.filter_by(user_id=user.id).all()
     return render_template('dashboard.html', user=user, orders=orders)
