import sys
from debate import *
from flask import Flask, jsonify, request
import re
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Get the JSON data and string from the request
    json_data = request.form.get('json_data')
    input_string = request.form.get('string_data')
    print(input_string)
    
    # Load the JSON data into a Python dictionary

    # Process the data as needed
    data = debate(input_string, json_data)
    
    return jsonify(data)

app.run(host='0.0.0.0', port=8003)
