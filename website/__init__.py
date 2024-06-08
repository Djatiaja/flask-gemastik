import flask 
import flask_cors as cors
import flask_sqlalchemy as sqlalchemy
import flask_login


db = sqlalchemy.SQLAlchemy()


def create_app():
    app = flask.Flask(__name__)
    cors.CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:asdf1234@localhost/users'
    app.config['SECRET_KEY'] = 'makanbang'
    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)
    db.init_app(app)
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from website.model import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    return app
