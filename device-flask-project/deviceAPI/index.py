import collect_data as cd 
import register_device as rd

from flask import Flask, jsonify, request
app = Flask(__name__)

devices = [ 
           
    {'u_id': 1, 'd_id': 1, 'd_type': "scale", 'd_mac': "00:00:11:11", 'd_firmware_v': "1.1.0", 'd_software_v': "1.1.0"}
           
]

device_data = [
    
    {'p_id': 1, 'd_id': 1, 'd_type': "scale", 'd': 133}
    
]


@app.route("/devices")
def get_devices():
    return jsonify(devices)

@app.route("/data")
def get_data():
    return jsonify(device_data)

@app.route("/devices", methods=['POST'])
def add_device():
    new_device = request.get_json()
    if rd.check_registration(new_device):
        devices.append(request.get_json())
    else: 
        return redirect
    return '', 204

@app.route("/data",methods=['POST'])
def add_data():
    new_data = request.get_json()
    if cd.check_collected_data(new_data):
        device_data.append(request.get_json())
    else: 
        return redirect
    return '', 204