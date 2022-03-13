import register_device as rd
import collect_data as cd 
import requests 
import json 

def ask_registration_input():
    u_id = input("what is the user id?: ")
    d_id = input("what is the device id?: ") 
    d_type = input("what is the device type?: ")
    d_mac = input("what is the device mac?: ")
    d_firmware_v = input("what is the device firmware version?: ")
    d_software_v = input("what is the device software version?: ")
    packaged = rd.register_device(int(u_id), int(d_id), d_type, d_mac, d_firmware_v, d_software_v)
    # if rd.check_registration(packaged) == True:
    #     return packaged
    # else:
    #     return "Invalid registration"
    return packaged
    
def ask_collection_info():
    p_id = input("what is the patient ID?: ")
    d_id = input("what is the device ID?: ")
    d_type = input("what is the device type?: ")
    d = input("Enter the data: ")
    packaged = cd.collect_data(int(p_id), int(d_id), d_type, int(d))
    # if cd.check_collected_data(packaged) == True:
    #     return cd.package_data(packaged)
    # else:
    #     return "Invalid data collection"
    return packaged
    
def main():
    url = "http://54.66.50.61:5000/"

    while(1):
        t = input("enter 'r' for registration and 'c' for data collection, 'vr' to view registrations and 'vc' to view data collections: ")
        if t == 'r':
            register = ask_registration_input()
            url1 = url + "devices"
            #register = rd.package_device_info(register)
            req = requests.post(url1, json=register)
            #print(req.status_code)
            print(req.text)
            
            
        if t == 'c':
            collect = ask_collection_info()
            url2 = url + "data"
            #collect = cd.package_data(collect)
            req = requests.post(url2, json=collect)
            #print(req.status_code)
            print(req.text)
            
        if t == 'vr': 
            url1 = url + "devices"
            req = requests.get(url1) 
            #print(req.status_code)
            print(req.text)
        
        if t == 'vc': 
            url2 = url + "data"
            req = requests.get(url2)
            #print(req.status_code)
            print(req.text)
    
if __name__ == "__main__":
    main()