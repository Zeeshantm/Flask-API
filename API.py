import sys
from flask import Flask, jsonify, request
import re

app = Flask(__name__)
# Set URL & Create Methods for Json Requests 
@app.route('/v1/sanitized/input', methods = ['GET', 'POST'])
def home():
    try:
    
        # Json Handler for GET Method
        if(request.method=='GET'):
            data  = "Get Method Working"
            return jsonify ({'Status':data})

        # Json Handler for POST Method
        elif(request.method=='POST'):
            req = request.json['payload']

            # Set SQL Injection Characters
            exp = re.compile('[!%&*()<>"/\\\|\':]')
        
            # Search for vulnerable characters  
            if(exp.search(req) == None):
                result = "Sanitized"
            else:
                result = "UnSanitized"

            # Return the Output
            return jsonify({'Result':result})

    except Exception as err:
        return jsonify ({'Error':"Execption in Handler "+err.__str__()})
        


    app.run()