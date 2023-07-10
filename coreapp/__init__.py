from flask import Flask
# from flask_migrate import Migrate
from coreapp.config import Configuration
from coreapp.db import db
from coreapp.restful_api.views import blueprint as service_app_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    # db.init_app(app)
    # migrate = Migrate(app, db)
    # подключаем блюпринт
    app.register_blueprint(service_app_blueprint)
    return app
