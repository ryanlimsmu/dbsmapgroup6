import os
from dotenv import load_dotenv
import mysql.connector

# Load environment variables
load_dotenv()

def create_app():
    from flask import Flask
    app = Flask(__name__)
    app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('FLASK_ENV') == 'development'

    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
        )
        print("Connection successful!")
    except Exception as e:
        print(f"Connection failed: {e}")

    return app, connection