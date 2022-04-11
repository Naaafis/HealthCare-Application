# HealthCare-Application

------------------------------------------------------------------------------------------------
Devices API

API is capable of uploading devices to a temporary databse and is currently hosted on AWS ec2 t2.micro instance
Functionalities involve being able to register a device, and being able to enter data for devices 
Error checks involve checking for all data types as well as checking that the correct device types are entered 
API also allows users to view all data that has been entered by far
Contact developer to reset data set with device and data information

To register a device the following parameters need to be provided: 
user_id, device_id, device_type, device_mac, firmware_v, software_v

To collect data for a device the following parameters need to be provided: 
patient_id, device_id, device_type, data

To Deploy API:
- cd to device-flask-project
- pip install pipenv
- pipenv --three
- pipenv install flask
- ./bootstrap.sh
- replace url in askinput.py outside this directory with directory of where API is running

------------------------------------------------------------------------------------------------

To use:
  - git clone this project and git checkout Devices
  - follow instructions to Deploy API and take note of URL running API
  - Replace url in line 33 of ask_input.py with above
  - cd out of device-flask-project directory and run the following command:
  - python ask_input.py 
  - test with any inputs you like for both viewing and registering devices and data collection, a temporary data structure is created by the API
