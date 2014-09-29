from flask import Flask, request, jsonify
from config import config
import os

app = Flask(__name__)
config_name = (os.getenv('FLASK_CONFIG') or 'default')
app.config.from_object(config[config_name])

@app.route('/move', methods=['POST'])
def move():
    movetype = request.json['type']
    duration = request.json['duration']
    return jsonify({ 'status' : 'success' }), 200

@app.route('/lights', methods=['POST'])
def lights():
    status = request.json['status']
    return jsonify({ 'status' : 'success' }), 200

@app.route('/beep', methods=['POST'])
def beep():
    duration = request.json['duration']
    return jsonify({ 'status' : 'success' }), 200

if __name__ == "__main__":
    app.run()