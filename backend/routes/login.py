from datetime import timedelta

from flask import Blueprint, request, jsonify
from routes.models import CompanyLogin
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

def loginFunction():
    data = request.get_json()
    username = data.get('username')  # Assuming username maps to EmployeeID
    password = data.get('password')  # Assuming password maps to Password

    # Check if user exists
    user = CompanyLogin.query.filter_by(username=username).first()

    if user:

        # Check if password is correct
        if user.password != password:
            return jsonify({"error": "Wrong password"}), 401
        
        else:
            access_token = create_access_token(
                identity=str(user.username),
                expires_delta=timedelta(hours=1),
                additional_claims={"roles": "ROLE_USER"}
            )
            return jsonify({"access_token": access_token, "message": f"Welcome, {user.username}!"}), 200
        
    else:
        return jsonify({"error": "Company not found"}), 404