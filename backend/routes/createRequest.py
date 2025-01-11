from flask import Blueprint, request, jsonify
from routes.models import db, OutstandingRequest,RequestReceived,CompanyAccount
from flask_jwt_extended import get_jwt_identity
from datetime import datetime, timedelta

def createRequestFunction(connection):
    try:
        # Retrieve the logged-in user's ID from the JWT
        user_id = get_jwt_identity()

        if not user_id:
            return jsonify({"error": "Unauthorized"}), 401
    

        data = request.get_json()  # Parse the JSON payload

        required_fields = ['companyId', 'carbonPrice', 'carbonQuantity', 'requestReason', 'requestType']
        for field in required_fields:
            if field not in  data:
                return jsonify({"error": f"Missing field: {field}"}), 422

        # Step 3: Create a new request for outstandingrequest
        new_outstanding_request = OutstandingRequest(
            companyId = data['companyID'],
            carbonUnitPrice = data['carbonPrice'],
            carbonQuantity = data['carbonQuantity'],
            requestReason = data['requestReason'],
            requestType = data['requestType'],
            createdDatetime = datetime.now(),
            updatedDatetime = datetime.now()
        )
        
        db.session.add(new_outstanding_request)

    

    
        # Step 4: Create a new request for requestreceived


        new_request = OutstandingRequest.query.filter(companyId = data['CompanyID'])\
        .filter(carbonUnitPrice = data['carbonPrice']).filter(carbonQuantity = data['carbonQuantity'])\
        .filter(requestReason = data['requestReason']).filter(requestType = data['requestType']).all()

        company_name = CompanyAccount.query.filter(companyId = data['CompanyID']).all()
                    
        new_request_received = RequestReceived(
            alertDatetime = datetime.now() + timedelta(days=7),
            alertText = f"Overdue Request {new_request['id']}: You have yet to approve {company_name}'s request to {new_request['requestType']} {new_request['carbonQuantity']} units of carbon at ${new_request['carbonUnitPrice']:.2f}.",
            alertStatus = "Scheduled",
            alertViewDate = None,
            createdDatetime = datetime.now(),
            updatedDatetime = datetime.now()
        )

        db.session.add(new_request_received)
        db.commit()
    
        return jsonify({"message": "Request added successfully!"}),200
 
    except Exception as e:
        print(f"Error in createRequest: {e}")
        return jsonify({"error": "Failed to process the request"}), 422
