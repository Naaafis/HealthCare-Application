#this is a function to collect data, check which device the data came from, and output a json file to be uploaded to the database


def collect_data(patient_id, device_id, device_type, data):
    #this function simply takes all the metrics for collecting data and returns a dictionary 
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    Dict = {'p_id': patient_id, 'd_id': device_id, 'd_type': device_type, 'd': data}
    return Dict

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

def package_data(inp):
    packet = json.dumps(inp)
    return packet