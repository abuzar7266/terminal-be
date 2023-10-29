from flask import Flask, request
from werkzeug.utils import secure_filename
import os
from .init import cli 

# Define the directory path where you want to save the files
UPLOAD_FOLDER = 'public/draw-chart'  # This should be the directory path

@cli.route('/upload', methods=['POST'])
def uploadDrawFile():
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        # You can access the file properties like filename, content type, and data
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        return f"{filename} has been uploaded successfully"
@cli.route('/list', methods=['GET'])
def getDrawFileList():
    file_names = [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]
    return file_names

@cli.route('/fetch', methods=['GET'])
def getDrawFile():
    return 'Get called for draw file save'

@cli.route('/remove', methods=['DELETE'])
def deleteDrawFile():
    return 'Delete called for draw file save'