from flask import Flask, jsonify, request
import pandas as pd
from werkzeug.utils import secure_filename
import os
from .init import cli 

# Define the directory path where you want to save the files
UPLOAD_FOLDER = 'public/draw-chart'  # This should be the directory path

def process_csv_file(csv_filename, selected_columns):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_filename)

        # Select the specified columns from the DataFrame
        selected_data = df[selected_columns]

        # Convert the selected data to a list of dictionaries
        data_list = selected_data.to_dict(orient='records')

        # Return the data as a JSON response
        return jsonify(data_list)
    except Exception as e:
        return jsonify({"error": str(e)})

@cli.route('/upload', methods=['POST'])
def uploadDrawFile():
    file = request.files['file']
    if file.filename == '':
        return jsonify({
            "status":"Error",
            "message": "No selected file"
        })
    
    if file:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        # You can access the file properties like filename, content type, and data
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        return jsonify({
            "status": "Success",
            "message": f"{file.filename} has been uploaded successfully"
        })
    
@cli.route('/list', methods=['GET'])
def getDrawFileList():
    file_names = [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]
    return file_names

@cli.route('/chart-data', methods=['GET'])
def getDrawFile():
    filename = request.args.get('filename')
    columns = request.args.get('columns').split(',')
    return process_csv_file(f'{UPLOAD_FOLDER}/{secure_filename(filename)}', columns)

def delete_draw_file(file_path):
    try:
        os.remove(f'{UPLOAD_FOLDER}/{secure_filename(file_path)}')
        status = "Success"
        message = f"File '{file_path}' has been successfully deleted."
    except Exception as e:
        status = "Error"
        message = f"Failed to delete file '{file_path}': {str(e)}"

    return status, message

@cli.route('/remove', methods=['DELETE'])
def deleteDrawFile():
    filename = request.args.get('filename')
    status, message = delete_draw_file(filename)
    return jsonify({
        "status": status,
        "message": message
    })