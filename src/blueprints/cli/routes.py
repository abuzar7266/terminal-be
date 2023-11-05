from flask import jsonify, request
from src.utils.constants import DEFAULT
from src.blueprints.cli.controllers import add_file, delete_draw_file, fetch_list_file, process_csv_file
from werkzeug.utils import secure_filename
from .init import cli 

@cli.route('/upload', methods=['POST'])
def upload_draw_file():
    file = request.files['file']
    return add_file(file)
    
@cli.route('/list', methods=['GET'])
def get_draw_file_list():
    return fetch_list_file()

@cli.route('/chart-data', methods=['GET'])
def get_draw_file():
    filename = request.args.get('filename')
    columns = request.args.get('columns').split(',')
    return process_csv_file(f'{DEFAULT.UPLOAD_FOLDER.value}/{secure_filename(filename)}', columns)

@cli.route('/remove', methods=['DELETE'])
def remove_draw_file():
    filename = request.args.get('filename')
    status, message = delete_draw_file(filename)
    return jsonify({
        "status": status,
        "message": message
    })