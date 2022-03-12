# import collect_data as cd 
# import register_device as rd

import json

from flask import Flask, jsonify, request
app = Flask(__name__)

devices = [ 
           
    {'u_id': 1, 'd_id': 1, 'd_type': "scale", 'd_mac': "00:00:11:11", 'd_firmware_v': "1.1.0", 'd_software_v': "1.1.0"}
           
]

device_data = [
    
    {'p_id': 1, 'd_id': 1, 'd_type': "scale", 'd': 133}
    
]

def check_registration(inp):
    user_id = inp['u_id']
    device_id = inp['d_id']
    device_type = inp['d_type']
    device_mac = inp['d_mac']
    firmware_v = inp['d_firmware_v']
    software_v = inp['d_software_v']
    
    if not isinstance(user_id, int):
        #no need to raise error since we are pytesting 
        #print("Please provide an integer indicating the id of a user")
        return "Please provide an integer indicating the id of a user"

    if not isinstance(device_id, int):
        #no need to raise error since we are pytesting 
        #print("Please provide an integer indicating the id of a device")
        return "Please provide an integer indicating the id of a device"

    if not isinstance(device_type, str):
        #no need to raise error since we are pytesting 
        #print("Please provide a string indicating the type of a device")
        return "Please provide a string indicating the type of a device"

    if not isinstance(device_mac, str):
        #no need to raise error since we are pytesting 
        #print("Please provide string indicating the device mac address")
        return "Please provide string indicating the device mac address"
    
    if not isinstance(firmware_v, str):
        #print("Please provide an integer indicating the firmware version")
        return "Please provide an integer indicating the firmware version"
    
    if not isinstance(software_v, str):
        #print("Please provide an integer indicating the software version")
        return "Please provide an integer indicating the software version"
    
    #sphygmomanometer measures blood pressure
    if device_type != "thermostat" and device_type != "sphygmomanometer" and device_type != "heart rate monitor" and device_type != "oximeter" and device_type != "glucometer" and device_type != "scale":
        #no need to raise error since we are pytesting 
        #print("please provide valid type of device")
        return "Please provide valid type of device"
    
    return "Valid Entry"

def check_collected_data(inp):  
    #this function is here to check if the user has provided valid input
    patient_id = inp['p_id']
    device_id = inp['d_id']
    device_type = inp['d_type']
    data = inp['d']  

    if not isinstance(patient_id, int):
        #no need to raise error since we are pytesting 
        #print("Please provide an integer indicating the id of a patient")
        return "Please provide an integer indicating the id of a patient"

    if not isinstance(device_id, int):
        #no need to raise error since we are pytesting 
        #print("Please provide an integer indicating the id of a device")
        return "Please provide an integer indicating the id of a device"

    if not isinstance(device_type, str):
        #no need to raise error since we are pytesting 
        #print("Please provide string indicating the type of a device")
        return "Please provide string indicating the type of a device"

    if not isinstance(data, int):
        #no need to raise error since we are pytesting 
        #print("Please provide an integer indicating the data")
        return "Please provide an integer indicating the data"

    ##sphygmomanometer measures blood pressure
    if device_type != "thermostat" and device_type != "sphygmomanometer" and device_type != "heart rate monitor" and device_type != "oximeter" and device_type != "glucometer" and device_type != "scale":
        #no need to raise error since we are pytesting 
        #print("please provide valid type of device")
        return "please provide valid type of device"
    
    return "Valid Entry"


@app.route("/devices", methods=["GET"])
def get_devices():
    return jsonify(devices)

@app.route("/data",methods=["GET"])
def get_data():
    return jsonify(device_data)

@app.route("/devices", methods=['POST'])
def add_device():
    new_device = request.get_json()
    if check_registration(new_device) == "Valid Entry":
        devices.append(request.get_json())
        return check_registration(new_device)
    else: 
        return check_registration(new_device)
    #return check_registration(new_device), 204

@app.route("/data",methods=['POST'])
def add_data():
    new_data = request.get_json()
    if check_collected_data(new_data) == "Valid Entry":
        device_data.append(request.get_json())
        return check_collected_data(new_data)
    else: 
        return check_collected_data(new_data)
    #return check_collected_data(new_data), 204

# @app.route("/data", methods=['GET'])
# def print_data():
#     count = 0
#     data = request.get_json()#still need to add indexing
#     print(data)