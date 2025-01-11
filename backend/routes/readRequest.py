from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from sqlalchemy.orm import joinedload

from routes.models import db, CompanyLogin, CompanyAccount, OutstandingRequest


def readRequestFunction():
    try:
        # Retrieve the logged-in user's ID from the JWT
        user_id = get_jwt_identity()

        if not user_id:
            return jsonify({"error": "Unauthorized"}), 401

        # Step 1: Fetch user to ensure they exist
        user = db.session.query(CompanyLogin).filter_by(id=user_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Step 2: Fetch requests associated with the user
        requests = (
            db.session.query(OutstandingRequest)
            .filter(OutstandingRequest.companyId == user_id)
            .all()
        )

        if not requests:
            # If no claims exist, return empty categories
            return jsonify({"message": "No requests found."}), 200

        # Step 3: Organize requests
        result = {"requests": []}

        for request in requests:
            request_data = {
                "id": request.id,
                "requestDate": request.createdDatetime,
                "companyName": request.requestorCompanyId,
                "carbonPrice": request.carbonUnitPrice,
                "carbonQuantity": request.carbonQuantity,
                "requestReason": request.requestReason,
                "requestType": request.requestType,
            }
            # Categorize claims based on status
            result["requests"].append(request_data)

        return jsonify(result), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to process the request"}), 422
