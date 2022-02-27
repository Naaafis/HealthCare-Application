import register_device as rd
import collect_data as cd 

def ask_registration_input():
    u_id = input("what is the user id?: ")
    d_id = input("what is the device id?: ") 
    d_type = input("what is the device type?: ")
    d_mac = input("what is the device mac?: ")
    d_firmware_v = input("what is the device firmware version?: ")
    d_software_v = input("what is the device software version?: ")
    packaged = rd.register_device(int(u_id), int(d_id), d_type, d_mac, d_firmware_v, d_software_v)
    if rd.check_registration(packaged) == True:
        return packaged
    else:
        return "Invalid registration"
    
def ask_collection_info():
    p_id = input("what is the patient ID?: ")
    d_id = input("what is the device ID?: ")
    d_type = input("what is the device type?: ")
    d = input("Enter the data: ")
    packaged = cd.collect_data(int(p_id), int(d_id), d_type, int(d))
    if cd.check_collected_data(packaged) == True:
        return cd.package_data(packaged)
    else:
        return "Invalid data collection"
    
def main():
    ask_registration_input()
    ask_collection_info()
    
if __name__ == "__main__":
    main()