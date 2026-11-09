from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api
from flask_httpauth import HTTPBasicAuth

db = SQLAlchemy()
api = Api()
auth = HTTPBasicAuth()
