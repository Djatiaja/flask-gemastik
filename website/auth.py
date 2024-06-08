from flask import Blueprint, request
from .model import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user,login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    email_exists = User.query.filter_by(Email=data['Email']).first()
    if email_exists:
        return 'Email already exists'
    user = User(Nama_lengkap=data['Nama_lengkap'], Email=data['Email'], Password=generate_password_hash(data['Password'], method="pbkdf2:sha256"))
    db.session.add(user)
    db.session.commit()
    return user.__repr__()

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(Email=data['Email']).first()
    if not user:
        return 'User not found'
    if check_password_hash(user.Password, data['Password']):
        login_user(user)
        return user.__repr__()
    return 'Wrong password'

@auth.route('/logout', methods=['POST', 'GET'   ])
@login_required
def logout():
    logout_user()
    return 'Logged out'

@auth.route('/api/status', methods=['GET'])
def status():
    if current_user.is_authenticated:
        return {'status': 'Logged in', 'user': current_user.__repr__()}
    return {'status': 'Not logged in'}

@auth.route('/api/user', methods=['GET'])
@login_required
def user():
    return current_user.__repr__()