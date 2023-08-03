import sys
from sentiment_splitter import *
from flask import Flask, jsonify, request
import re
import json

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def home():
    link = request.json
    data = split(link)
    return data

app.run(host='0.0.0.0',port=8001,debug=True)



