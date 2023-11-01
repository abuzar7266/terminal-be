from flask import Blueprint, Flask
from src.blueprints.cli.init import cli
from flask_cors import CORS, cross_origin

def create_app():
    app = Flask(__name__)
    CORS(app, support_credentials=True)
    app.config['UPLOAD_FOLDER'] = "draw-chart"
    app.register_blueprint(cli, url_prefix='/cli')

    return app