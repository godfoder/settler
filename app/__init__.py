from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object('app.config')
db = SQLAlchemy(app)

from app.views import index

from app.models import user, role

user_datastore = SQLAlchemyUserDatastore(db, user.User, role.Role)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    try:
        user_datastore.create_user(email='godfoder@gmail.com', password='password')
        db.session.commit()
    except:
        db.session.rollback()