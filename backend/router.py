from flask import Blueprint, request, jsonify
from routes.createRequest import createRequestFunction
from routes.deleteRequest import deleteRequestFunction
from routes.login import loginFunction
from routes.readAccount import readAccountFunction
from routes.readIncoming import readIncomingFunction
from routes.readRequest import readRequestFunction
from routes.updateIncoming import updateIncomingFunction
from routes.updateRequest import updateRequestFunction

posts = Blueprint('posts', __name__)

def configure_routes(app, connection):
    # Please update the route and method
    @app.route('/api/posts', methods=['GET'])
    def createRequest():
        createRequestFunction(connection)

    # Please update the route and method
    @app.route('/api/posts', methods=['GET'])
    def deleteRequest():
        deleteRequestFunction(connection)
    
    # Please update the route and method
    @app.route('/api/posts', methods=['GET'])
    def login():
        loginFunction(connection)
        
    # Please update the route and method
    @app.route('/api/posts', methods=['GET'])
    def readAccount():
        readAccountFunction(connection)
    
    # Please update the route and method
    @app.route('/api/posts', methods=['GET'])
    def readIncoming():
        readIncomingFunction(connection)

    # Please update the route and method
    @app.route('/api/posts', methods=['GET'])
    def readRequest():
        readRequestFunction(connection)

    # Please update the route and method
    @app.route('/api/posts', methods=['GET'])
    def updateIncoming():
        updateIncomingFunction(connection)

    # Please update the route and method
    @app.route('/api/posts', methods=['GET'])
    def updateRequest():
        updateRequestFunction(connection)