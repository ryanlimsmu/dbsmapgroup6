from flask import Blueprint, request, jsonify
from backend.routes.models import db, CompanyAccount
from flask_jwt_extended import get_jwt_identity

def readAccountFunction(connection):
    try:
        # Retrieve the logged-in user's ID from the JWT
        user_id = get_jwt_identity()

        if not user_id:
            return jsonify({"error": "Unauthorized"}), 401
        
        data = request.get_json  # Parse the JSON payload
        id = data.get('id')

        user = CompanyAccount.query.filter_by(companyId=id).all()
        result = [user.companyName, user.carbonBalance,user.cashBalance]
        # All the functions

        return jsonify(result),200

    except Exception as e:
        print(f"Error in readAccount: {e}")
        return jsonify({"error": "Failed to process the request"}), 422
