from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from routes.models  import db, CompanyAccount

def updateRequestFunction():
    company_id = get_jwt_identity()
    # Just template
    data = request.json  # Parse the JSON payload
    username = data.get('username')

    user = CompanyAccount.query.filter_by(companyId=username).first()

    # All the functions

    return jsonify({}),200