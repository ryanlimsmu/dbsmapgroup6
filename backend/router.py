from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required

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
    @jwt_required()
    def readAccount():
        return readAccountFunction(connection)
    
    # 3
    @app.route('/createRequest', methods=['GET'])
    @jwt_required()
    def createRequest():
        return createRequestFunction(connection)
    
    # 4
    @app.route('/readRequests', methods=['GET'])
    @jwt_required()
    def readRequest():
        return readRequestFunction(connection)
    
    # 5
    @app.route('/updateRequest', methods=['GET'])
    @jwt_required()
    def updateRequest():
        return updateRequestFunction(connection)

    # 6
    @app.route('/deleteRequest/<int:request_id>', methods=['DELETE'])
    @jwt_required()
    def deleteRequest(request_id):
        return deleteRequestFunction(connection)
    
    # 7
    @app.route('/readIncoming', methods=['GET'])
    @jwt_required()
    def readIncoming():
        return readIncomingFunction(connection)

    # 8
    @app.route('/updateIncoming/<int:request_id>', methods=['PUT'])
    @jwt_required()
    def updateIncoming(request_id):
        return updateIncomingFunction(connection)
    
    # 9
    @app.route('/readAlerts', methods=['GET'])
    @jwt_required()
    def readAlerts():
        return readAlertsFunction(connection)
    
    # 10
    @app.route('/updateAlerts/<int:request_id>', methods=['PUT'])
    @jwt_required()
    def updateAlerts(request_id):
        return updateAlertsFunction(connection)
    
    # 11
    @app.route('/readAllCompanies', methods=['GET'])
    @jwt_required()
    def readAllCompanies():
        return readAllCompaniesFunction(connection)