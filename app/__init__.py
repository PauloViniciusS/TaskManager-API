from flask import Flask
from app.config import Config
from app.extensions import db
from app.extensions import api

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app import models

    from app.resources.tasks import blp as tasks_blp

    api.register_blueprint(tasks_blp)
    
    return app