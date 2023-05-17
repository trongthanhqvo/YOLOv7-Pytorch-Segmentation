import io
import requests
from flask import Flask, request, jsonify, make_response
import base64
import time
from datetime import datetime

def print_current_time():
    now = datetime.now()
    print(now)

app = Flask(__name__)

@app.route("/processeBuffer", methods=["POST"])
def Prossece_Buffer():
    try:
        print_current_time()
        print(request.path)
        #return "hello world"
        data = request.json
        # print("Data:", data)
        # return {"data":"Succesess"}
        #return "hello world" 
        sample = data.get("sample", "")
        print(len(sample))
        if sample == "": return {"data": "fail"}
        return {"data": "true"}
    except Exception as ex:
        print("Exception:", ex)
