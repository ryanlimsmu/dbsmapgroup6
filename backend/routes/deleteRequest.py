from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from routes.models import db, OutstandingRequest


def deleteRequestFunction(request_id):
    try:
        # Step 1: Retrieve the logged-in user's ID from the JWT
        user_id = get_jwt_identity()
        if not user_id:
            return jsonify({"error": "Unauthorized"}), 401

        # Step 2: Retrieve the request and ensure it belongs to the logged-in user
        requests = (
            db.session.query(OutstandingRequest)
            .filter(OutstandingRequest.companyId == user_id)
            .all()
        )

        if not requests:
            return jsonify({"error": "Request not found or not authorized"}), 404

        # Step 3: Delete the claim
        db.session.delete(request_id)
        db.session.commit()
        return jsonify({"message": "Claim deleted successfully!"}), 200

    except Exception as e:
        print(f"Error in delete_claim: {e}")
        return jsonify({"error": "Failed to delete the claim"}), 500
