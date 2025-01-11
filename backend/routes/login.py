from datetime import timedelta

from flask import Blueprint, request, jsonify
from models import CompanyLogin
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

def loginFunction():
    data = request.get_json()
    username = data.get('username')  # Assuming username maps to EmployeeID
    password = data.get('password')  # Assuming password maps to Password

    user = CompanyLogin.query.filter_by(companyUsername=username, companyPassword=password).first()

    if user:
        access_token = create_access_token(
            identity=str(user.companyUsername),
            expires_delta=timedelta(hours=1),
            additional_claims={"roles": "ROLE_USER"}
        )
        return jsonify({"access_token": access_token, "message": f"Welcome, {user.FirstName}!"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401