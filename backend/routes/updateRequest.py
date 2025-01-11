from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from routes.models  import db, OutstandingRequest


def updateRequestFunction(request_id):
    try:
        # Step 1: Retrieve the logged-in user's ID from the JWT
        user_id = get_jwt_identity()
        if not user_id:
            return jsonify({"error": "Unauthorized update request"}), 401

        # Step 2: Retrieve the claim and ensure it belongs to the logged-in user
        request = db.session.query(OutstandingRequest).filter(
            OutstandingRequest.id == request_id,
            OutstandingRequest.companyId == user_id
        ).first()

        if not request:
            return jsonify({"error": "Claim not found or not authorized"}), 404

        # Step 4: Update the request based on the request data
        data = request.get_json()
        if 'requestId' in data:
            request.id = data.get('requestId', request.id)
        if 'companyId' in data:
            request.companyId = data.get('companyId', request.companyId)
        if 'carbonUnitPrice' in data:
            request.carbonUnitPrice = data.get('carbonUnitPrice', request.carbonUnitPrice)
        if 'carbonQuantity' in data:
            request.carbonQuantity = data.get('carbonQuantity', request.carbonQuantity)
        if 'requestReason' in data:
            request.requestReason = data.get('requestReason', request.requestReason)
        if 'requestType' in data:
            request.requestType = data.get('requestType', request.requestType)

        request.updatedDatetime = datetime.now()

        db.session.commit()

        return jsonify({"message": "Claim updated successfully!"}), 200

    except Exception as e:
        print(f"Error in update_claim: {e}")
        return jsonify({"error": "Failed to update the claim"}), 500
