from flask import Blueprint, Flask
from src.blueprints.cli.init import cli

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = "draw-chart"
    app.register_blueprint(cli, url_prefix='/cli')

    return app