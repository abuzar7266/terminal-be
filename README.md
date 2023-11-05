# Terminal Backend (terminal-be) README

Welcome to the README for the Terminal Backend (terminal-be), an API application developed in Flask. This document will provide you with the necessary instructions to set up and run the backend in development mode, an overview of its code structure, and additional information about its deployment.

## Getting Started

To run this backend API application in development mode, please follow these steps:

1. **Clone the Repository:**
   Clone the `terminal-be` project repository.

2. **Go to Project Root Directory:**
   Navigate to the project's root directory.

3. **Install Python Dependencies:**
   Use the following command to install all the Python dependencies listed in the `requirements.txt` file: pip install -r requirements.txt

4. **Start the Development Server:**
Run the development server using the following command to start your Flask server: flask run --host=0.0.0.0 --port=8080


Your Flask server will start running.

5. **Environment Variables:**
A `.env` file containing `FLASK_APP=src.api.init` must be included in the project for the Flask app to run.

## Code Structure

The code for the Terminal Backend is structured as follows:

- **public:** This folder contains public data.

- **src:** This directory contains the source code of the Flask application.

- **src/api:** This directory includes the `init` file, a config file with app configuration settings, and a routes file that registers all the routes. This directory contains all the main files required for the Flask app. The `init.py` is the main file that Flask will execute.

- **src/blueprints:** This directory contains all the routes defined and their controller functions. The `init` file is used to create a routes registry.

- **src/utils:** This directory contains helper functions, constants, and other utility files.

## Deployment

The Flask app is currently deployed on an EC2 server, and it can be accessed at the following URL:

[Terminal Backend on EC2](http://ec2-52-202-69-19.compute-1.amazonaws.com:8080)

Please note that the app is running in development mode inside the EC2 machine. However, the deployed backend is not able to connect with the `terminal-fe` application due to insufficient configurations on the EC2 instance. You can test the API using Postman or other API testing tools.

Thank you for using the Terminal Backend! If you have any questions or encounter any issues, please feel free to reach out to the development team.




