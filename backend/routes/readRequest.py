from flask import Blueprint, request, jsonify
from backend.routes.models import db, CompanyAccount

def readRequestFunction(connection):
    # Just template
    data = request.json  # Parse the JSON payload
    username = data.get('username')

    user = CompanyAccount.query.filter_by(companyId=username).first()

    # All the functions

    return jsonify({}),200