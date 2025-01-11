from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager

from routes.createRequest import createRequestFunction
from routes.deleteRequest import deleteRequestFunction
from routes.login import loginFunction
from routes.readAccount import readAccountFunction
from routes.readIncoming import readIncomingFunction
from routes.readRequest import readRequestFunction
from routes.updateIncoming import updateIncomingFunction
from routes.updateRequest import updateRequestFunction
from routes.readAlerts import readAlertsFunction
from routes.updateAlerts import updateAlertsFunction
from routes.readAllCompanies import readAllCompaniesFunction

posts = Blueprint('posts', __name__)
jwt = JWTManager()

def configure_routes(app, connection):
    
    # 1
    @app.route('/login', methods=['POST'])
    def login():
        return loginFunction()
    
    # 2
    @app.route('/readAccount', methods=['GET'])
    def readAccount():
        return readAccountFunction(connection)
    
    # 3
    @app.route('/createRequest', methods=['GET'])
    def createRequest():
        return createRequestFunction(connection)
    
    # 4
    @app.route('/readRequests', methods=['GET'])
    def readRequest():
        return readRequestFunction(connection)
    
    # 5
    @app.route('/updateRequest', methods=['GET'])
    def updateRequest():
        return updateRequestFunction(connection)

    # 6
    @app.route('/deleteRequest', methods=['GET'])
    @app.route('/deleteRequst/<int:request_id>', methods=['DELETE'])
    def deleteRequest(request_id):
        return deleteRequestFunction(connection)
    
    # 7
    @app.route('/readIncomings', methods=['GET'])
    def readIncoming():
        return readIncomingFunction(connection)

    # 8
    @app.route('/updateIncoming/<int:request_id>', methods=['PUT'])
    def updateIncoming(request_id):
        return updateIncomingFunction(connection)
    
    # 9
    @app.route('/readAlerts', methods=['GET'])
    def readAlerts():
        return readAlertsFunction(connection)
    
    # 10
    @app.route('/updateAlerts', methods=['GET'])
    def updateAlerts():
        return updateAlertsFunction(connection)
    
    # 11
    @app.route('/readAllCompanies', methods=['GET'])
    def readAllCompanies():
        return readAllCompaniesFunction(connection)