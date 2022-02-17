#this function exists to register a new device to a user and verify the registration information


#this is a function for an administratice user to add a device to the system
def register_device(user_id, device_id, device_type, device_mac, firmware_v, software_v):
    #creare a data structure to take in all user information and output a dictionary of the information
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    Dict = {'u_id': user_id, 'd_id': device_id, 'd_type': device_type, 'd_mac': device_mac, 'd_firmware_v': firmware_v, 'd_software_v': software_v}
    return Dict

def check_registration(inp):
    user_id = inp['u_id']
    device_id = inp['d_id']
    device_type = inp['d_type']
    device_mac = inp['d_mac']
    firmware_v = inp['d_firmware_v']
    software_v = inp['d_software_v']
    
    if not isinstance(user_id, int):
        #no need to raise error since we are pytesting 
        print("Please provide an integer indicating the id of a user")
        return False

    if not isinstance(device_id, int):
        #no need to raise error since we are pytesting 
        print("Please provide an integer indicating the id of a device")
        return False

    if not isinstance(device_type, str):
        #no need to raise error since we are pytesting 
        print("Please provide a string indicating the type of a device")
        return False

    if not isinstance(device_mac, str):
        #no need to raise error since we are pytesting 
        print("Please provide string indicating the device mac address")
        return False
    
    if not isinstance(firmware_v, int):
        print("Please provide an integer indicating the firmware version")
        return False
    
    if not isinstance(software_v, int):
        print("Please provide an integer indicating the software version")
        return False
    
    #sphygmomanometer measures blood pressure
    if(device_type != "thermostat" && device_type != "sphygmomanometer" && device_type != "heart rate monitor" && device_type != "oximeter" && device_type != "glucometer" && device_type != "scale"):
        #no need to raise error since we are pytesting 
        print("please provide valid type of device")
        return False
    
    return True
    
def package_device_info(inp):
    packet = json.dumps(inp)
    return packet