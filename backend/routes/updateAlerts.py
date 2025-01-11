from datetime import datetime

from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity

from backend.routes.models import OutstandingRequest, db


def updateAlertsFunction(request_id):
    try:
        # Step 1: Retrieve the logged-in user's ID from the JWT
        user_id = get_jwt_identity()
        if not user_id:
            return jsonify({"error": "Unauthorized"}), 401

        # Step 2: Retrieve the claim and ensure it belongs to the logged-in user
        request = db.session.query(OutstandingRequest).filter(
            OutstandingRequest.id == request_id,
            OutstandingRequest.companyId == user_id
        ).first()

        if not request:
            return jsonify({"error": "Claim not found or not authorized"}), 404

        # Step 4: Update the request status
        data = request.get_json()
        request.id = data.get('alertId', request.id)
        request.Status = data.get('alertStatus', request.Status)
        request.LastEditedClaimDate = datetime.now()

        db.session.commit()

        return jsonify({"message": "Alert updated successfully!"}), 200

    except Exception as e:
        print(f"Error in update_claim: {e}")
        return jsonify({"error": "Failed to update the claim"}), 500