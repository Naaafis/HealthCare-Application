from .collect_data import collect_data as cd 
from .register_device import register_device as rd

import json

from flask import Flask, jsonify, request
app = Flask(__name__)

devices = [ 
           
    {'u_id': 1, 'd_id': 1, 'd_type': "scale", 'd_mac': "00:00:11:11", 'd_firmware_v': "1.1.0", 'd_software_v': "1.1.0"}
           
]

device_data = [
    
    {'p_id': 1, 'd_id': 1, 'd_type': "scale", 'd': 133}
    
]

def check_collected_data(inp):  
    #this function is here to check if the user has provided valid input
    patient_id = inp['p_id']
    device_id = inp['d_id']
    device_type = inp['d_type']
    data = inp['d']  

    if not isinstance(patient_id, int):
        #no need to raise error since we are pytesting 
        print("Please provide an integer indicating the id of a patient")
        return False

    if not isinstance(device_id, int):
        #no need to raise error since we are pytesting 
        print("Please provide an integer indicating the id of a device")
        return False

    if not isinstance(device_type, str):
        #no need to raise error since we are pytesting 
        print("Please provide string indicating the type of a device")
        return False

    if not isinstance(data, int):
        #no need to raise error since we are pytesting 
        print("Please provide an integer indicating the data")
        return False

    ##sphygmomanometer measures blood pressure
    if device_type != "thermostat" and device_type != "sphygmomanometer" and device_type != "heart rate monitor" and device_type != "oximeter" and device_type != "glucometer" and device_type != "scale":
        #no need to raise error since we are pytesting 
        print("please provide valid type of device")
        return False
        
    return True


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
    if check_collected_data(new_data):
        device_data.append(request.get_json())
    else: 
        check_collected_data(new_data)
    return 'hi shim'

@app.route("/data", methods=['GET'])
def print_data():
    count = 0
    data = request.get_json()#still need to add indexing
    print(data)