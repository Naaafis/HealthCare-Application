#this is a function for an administratice user to add a device to the system

def register_device(id_list, device_name, device_mac, device_user, firmware_v, software_v, DOP):
    #create a query for assigning each of these attributes and output a data structure that ccan be used to update the database