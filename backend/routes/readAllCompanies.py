from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from routes.models  import db, CompanyAccount

def readAllCompaniesFunction(connection):
    data = request.get_json()

    # JWT Authentication
    companyId = get_jwt_identity()

    if companyId is None:
        return jsonify({'error': 'Unauthorized read request'}), 401

    # Retrieve all companies from the database that is not the current company
    companies = CompanyAccount.query.filter(CompanyAccount.companyId != companyId).all()

    companiesList = []
    for company in companies:
        companiesList.append({
            'companyId': company.companyId,
            'companyName': company.companyName
        })
    
    return jsonify(companiesList), 200