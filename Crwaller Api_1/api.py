import sys
from scraper import *
from flask import Flask, jsonify, request
import re
import json
from clean import *
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    link = request.args.get('url')
    Scrapped_data = scrape(link).splitlines()
    clean_data = clean(Scrapped_data)
    # res = requests.post('http://127.0.0.1:8001', json=lines)
    # res_from_splitter = res.json()
    # query = "Global warming is really bad"
    # Serialize the JSON data to a string
    # json_data_str = json.dumps(res_from_splitter)

    # Create a dictionary with the JSON data and string
    # data = {
    #     'json_data': json_data_str,
    #     'string_data': query
    # }
    
    # res = requests.post("http://127.0.0.1:8003", data=data)

    return clean_data

app.run(host='0.0.0.0', port=8001)
