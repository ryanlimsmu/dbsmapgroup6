import os
from dotenv import load_dotenv
import mysql.connector
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
from flask_jwt_extended import JWTManager

>>>>>>> Stashed changes
=======
from flask_jwt_extended import JWTManager

>>>>>>> Stashed changes
from routes.models import db

# Load environment variables
load_dotenv()

def create_app():
    from flask import Flask
    app = Flask(__name__)
    app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('FLASK_ENV') == 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
        )
        db.init_app(app)
        jwt = JWTManager(app)
        print("Connection successful!")
    except Exception as e:
        print(f"Connection failed: {e}")

    return app, connection