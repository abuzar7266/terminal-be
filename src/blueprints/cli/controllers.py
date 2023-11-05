import os
from src.utils.constants import DEFAULT
from werkzeug.utils import secure_filename
from flask import jsonify
import pandas as pd


def add_file(file):
    if file.filename == '':
        return jsonify({
            "status":"Error",
            "message": "No selected file"
        })
    
    if file:
        if not os.path.exists(DEFAULT.UPLOAD_FOLDER.value):
            os.makedirs(DEFAULT.UPLOAD_FOLDER.value)
        # You can access the file properties like filename, content type, and data
        filename = secure_filename(file.filename)
        file_path = os.path.join(DEFAULT.UPLOAD_FOLDER.value, filename)
        file.save(file_path)
        return jsonify({
            "status": "Success",
            "message": f"{file.filename} has been uploaded successfully"
        })
    
def fetch_list_file():
    return [f for f in os.listdir(DEFAULT.UPLOAD_FOLDER.value) if os.path.isfile(os.path.join(DEFAULT.UPLOAD_FOLDER.value, f))]


def delete_draw_file(file_path):
    try:
        os.remove(f'{DEFAULT.UPLOAD_FOLDER.value}/{secure_filename(file_path)}')
        status = "Success"
        message = f"File '{file_path}' has been successfully deleted."
    except Exception as e:
        status = "Error"
        message = f"Failed to delete file '{file_path}': {str(e)}"

    return status, message


def process_csv_file(csv_filename, selected_columns):
    try:
        df = pd.read_csv(csv_filename)
        selected_data = df[selected_columns]
        data_list = selected_data.to_dict(orient='records')
        return jsonify(data_list)
    except Exception as e:
        return jsonify({"error": 'Failed to fetch the data'})