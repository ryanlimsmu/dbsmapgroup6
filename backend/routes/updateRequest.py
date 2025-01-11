from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from routes.models  import db, CompanyAccount

def updateRequestFunction():
    company_id = get_jwt_identity()

    # Just template
    data = request.json  # Parse the JSON payload
    username = data.get('username')
    user = CompanyAccount.query.filter_by(companyId=username).first()
    # End of template

    try:
        # Step 1: Get the logged-in user's ID from the JWT
        user_id = get_jwt_identity()
        print(f"User ID from token: {user_id}")  # Debugging

        # Step 2: Validate the input data (support both JSON and form data)
        data = request.get_json() if request.is_json else request.form

        required_fields = ['ProjectID', 'CurrencyID', 'ExpenseDate', 'Amount', 'Purpose', 'Status']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 422

        # Step 3: Create a new claim
        new_claim = ProjectExpenseClaims(
            ProjectID=data['ProjectID'],
            EmployeeID=user_id,
            CurrencyID=data['CurrencyID'],
            ExpenseDate=datetime.strptime(data['ExpenseDate'], '%Y-%m-%d'),
            Amount=data['Amount'],
            Purpose=data['Purpose'],
            ChargeToDefaultDept=data.get('ChargeToDefaultDept', 'false').lower() == 'true',  # Convert to boolean
            AlternativeDeptCode=data.get('AlternativeDeptCode', ''),
            Status=data['Status'],
            LastEditedClaimDate=datetime.now()
        )


        db.session.add(new_claim)
        db.session.commit()

        return jsonify({"message": "Claim created successfully!", "ClaimID": new_claim.ClaimID}), 201

    except Exception as e:
        print(f"Error in create_claim: {e}")
        return jsonify({"error": "Failed to create claim"}), 500