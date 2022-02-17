import register_device as rd
import collect_data as cd 
from datetime import datetime
import codecs
#import logging

#this function exists to test that the data collection and device registration metrics work properly
def test_register_device():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    test_dict = {'u_id': 001, 'd_id': 001, 'd_type': "scale", 'd_mac': "00:00:11:11", 'd_firmware_v': 1.1.0, 'd_software_v': 1.1.0, 'registered_time': current_time}
    func_dict = rd.register_device(001, 001, "scale", "00:00:11:11", 1.1.0, 1.1.0)
    assert test_dict['u_id'] == func_dict['u_id'], "Failed to register user ID"
    assert test_dict['d_id'] == func_dict['d_id'], "Failed to register device ID"
    assert test_dict['d_type'] == func_dict['d_type'], "Failed to register device type"
    assert test_dict['d_mac'] == func_dict['d_mac'], "Failed to register device MAC"
    assert test_dict['d_firmware_v'] == func_dict['d_firmware_v'], "Failed to register device firmware"
    assert test_dict['d_software_v'] == func_dict['d_software_v'], "Failed to register device software"
   
#the functions arent testing for accuracy in time because it may differ by seconds
def test_collect_data():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    test_dict = {'p_id': 001, 'd_id': 001, d_type: "scale", d: 133, 'time': current_time}
    func_dict = cd.collect_data(001, 001, "scale", 133)
    assert test_dict['u_id'] == func_dict['u_id'], "Failed to collect user ID"
    assert test_dict['d_id'] == func_dict['d_id'], "Failed to collect device ID"
    assert test_dict['d_type'] == func_dict['d_type'], "Failed to collect device type"
    assert test_dict['d'] == func_dict['d'], "Failed to collect data"
    
#these functions exist to check that json collectin works properly
def test_package_device_info():
    func_dict = rd.register_device(001, 001, "scale", "00:00:11:11", 1.1.0, 1.1.0)
    jsonpack = rd.package_device_info(func_dict)
    testjson = json.dumps(jsonpack)
    assert testjson['u_id'] == func_dict['u_id'], "Failed to register json user ID"
    assert testjson['d_id'] == func_dict['d_id'], "Failed to register json device ID"
    assert testjson['d_type'] == func_dict['d_type'], "Failed to register json device type"
    assert testjson['d_mac'] == func_dict['d_mac'], "Failed to register json device mac address"
    assert testjson['d_firmware_v'] == func_dict['d_firmware_v'], "Failed to register json device firmware version"
    assert testjson['d_software_v'] == func_dict['d_software_v'], "Failed to register json device software version"
    
def test_package_data():
    func_dict = cd.collect_data(001, 001, "scale", 133)
    jsonpack = cd.package_data(func_dict)
    testjson = json.dumps(jsonpack)
    assert testjson['u_id'] == func_dict['u_id'], "Failed to collect json user ID"
    assert testjson['d_id'] == func_dict['d_id'], "Failed to collect json device ID"
    assert testjson['d_type'] == func_dict['d_type'], "Failed to collect json device type"
    assert testjson['d'] == func_dict['d'], "Failed to collect json data"
    
#these functions exist to test the chcking functions 
def test_check_registration():
    func_dict = rd.register_device(001, 001, "scale", "00:00:11:11", 1.1.0, 1.1.0)
    test = rd.check_registration(func_dict)
    assert test == True, "Failed to check registration"
    func_dict = rd.register_device("001", 001, "scale", "00:00:11:11", 1.1.0, 1.1.0)
    test = rd.check_registration(func_dict)
    assert test == False, "Failed to check registration"
    func_dict = rd.register_device(001, "001", "scale", "00:00:11:11", 1.1.0, 1.1.0)
    test = rd.check_registration(func_dict)
    assert test == False, "Failed to check registration"
    func_dict = rd.register_device(001, 001, 133, "00:00:11:11", 1.1.0, 1.1.0)
    test = rd.check_registration(func_dict)
    assert test == False, "Failed to check registration"
    func_dict = rd.register_device(001, 001, "dollar", "00:00:11:11", 1.1.0, 1.1.0)
    test = rd.check_registration(func_dict)
    assert test == False, "Failed to check registration"
    func_dict = rd.register_device(001, 001, "scale", 00:00:11:11, 1.1.0, 1.1.0)
    test = rd.check_registration(func_dict)
    assert test == False, "Failed to check registration"
    func_dict = rd.register_device(001, 001, "scale", "00:00:11:11", "1.1.0", 1.1.0)
    test = rd.check_registration(func_dict)
    assert test == False, "Failed to check registration"
    func_dict = rd.register_device(001, 001, "scale", "00:00:11:11", 1.1.0, "1.1.0")
    test = rd.check_registration(func_dict)
    assert test == False, "Failed to check registration"
    
def test_check_collected_data():
    func_dict = cd.collect_data(001, 001, "scale", 133)
    test = cd.check_collected_data(func_dict)
    assert test == True, "Failed to check collected data"
    func_dict = cd.collect_data("001", 001, "scale", 133)
    test = cd.check_collected_data(func_dict)
    assert test == False, "Failed to check collected data"
    func_dict = cd.collect_data(001, "001", "scale", 133)
    test = cd.check_collected_data(func_dict)
    assert test == False, "Failed to check collected data"
    func_dict = cd.collect_data(001, 001, "haha", 133)
    test = cd.check_collected_data(func_dict)
    assert test == False, "Failed to check collected data"
    func_dict = cd.collect_data(001, 001, 133, 133)
    test = cd.check_collected_data(func_dict)
    assert test == False, "Failed to check collected data"
    func_dict = cd.collect_data(001, 001, "scale", "133")
    test = cd.check_collected_data(func_dict)
    assert test == False, "Failed to check collected data"
    
#not creating main function for now