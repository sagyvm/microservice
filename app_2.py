# your app.py
import os
import requests

from flask import Flask, g,request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/static/api/2', methods=['GET'])
def getPhoto():
    return jsonify({'data': 'success'})




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)

