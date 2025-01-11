from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from routes.models  import db, OutstandingRequest

def readIncomingFunction(connection):
    data = request.get_json()

    # JWT Authentication
    companyId = get_jwt_identity()

    if companyId is None:
        return jsonify({'error': 'Unauthorized read request'}), 401
    
    # Retrieve all incoming outstanding requests from the database (with requestStatus = 'Pending') corresponding to the current company
    requests = OutstandingRequest.query.filter(OutstandingRequest.companyId == companyId, OutstandingRequest.requestStatus == 'Pending').all()

    requestsList = []
    for request in requests:
        requestsList.append({
            'requestId': request.id,
            'requestDatetime': request.requestDatetime,
            'companyId': request.requestorcompanyId,
            'carbonUnitPrice': request.carbonUnitPrice,
            'carbonQuantity': request.carbonQuantity,
            'requestReason': request.requestReason,
            'requestType': request.requestType
        })
    
    return jsonify(requestsList), 200