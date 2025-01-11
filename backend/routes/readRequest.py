from flask import Blueprint, request, jsonify

def createRequestFunction(connection):
    # Just template
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM posts;")
        result = cursor.fetchall()
        cursor.close()
    return result,200
 