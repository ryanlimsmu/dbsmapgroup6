from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from routes.models  import db, RequestReceived
from datetime import datetime

def readAlertsFunction(connection):

    # Obtain request IDs (expect array of request IDs)
    data = request.get_json()
    requestIds = data.get('requestIds')

    # JWT Authentication
    companyId = get_jwt_identity()

    if companyId is None:
        return jsonify({'error': 'Unauthorized read request'}), 401
    
    # Retrieve all alerts from the database corresponding to the request IDs
    alerts = RequestReceived.query.filter(RequestReceived.requestId.in_(requestIds)).all()

    # Filter out alerts that have alertDatetime in the past
    alerts = [alert for alert in alerts if alert.alertDatetime >= datetime.now()]

    alertsList = []
    for alert in alerts:
        alertsList.append({
            'alertId': alert.alertId,
            'requestId': alert.requestId,
            'alertDatetime': alert.alertDatetime,
            'alertText': alert.alertText,
            'alertStatus': alert.alertStatus
        })
    
    return jsonify(alertsList), 200