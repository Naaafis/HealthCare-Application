# HealthCare-Application

Branching Strategy:

- Each branch represents the development of individual modules
- Devices: Branch for development of device data collection module. Associates individual devices with users and identifies devices. Holds programs to send collected data to proper database section.
- Chat: Branch for deveopment of chat module. Associates users with messages they send, and holds secure messaging program. Identifies who can message who, and give admins power to broadcast messages.  
- Calendar: Branch for development of calender module. Holds program for calender interface, associates each user with a calender, uploads/updates proper section of database for calenders. 
- Voice Transcriber: Branch for development of speech to text module. This interface should be available to all users and it will be a navigation feature to the overall application.
- Alerts: Branch for development of alerts module. Gives access to administrative users to be able to send these alerts. 
- Administrative: Branch for development of administration module. This branch holds configuration programs that allow one to add people to the system, and thus the database. 
- Data Management: Branch for development of database module. This branch is used to delpoy our database, configure database, and design schema for database. 
- Application: Branch for development of application interface. Connects development progress of all other branches. 


------------------------------------ Product Description ------------------------------------------

Platform to monitor patients at home or in the hospitals

Users:
- Patients
- Medical Professionals (Nurses and Doctors)
- Administrators
- Developers:
  - Application developers 
  - Device integrators
  - Machine Learning Scientists

Users Table Content:
- User_ID
- Personal Information
  - DOB
  - Address
  - Primary care provider
  - Billing Info
  - Family members
  - Emergency Contacts
  - Medical Card
  - Insurance
   
- Medical History
  - Height 
  - Weight
  - Gender
  - Medications 
  - Allergy



Device Table Content:
- Device type
- Device ID
- Device MAC Addr
- User it belongs to ID
- Firmware version
- Software version
- Date of Purchase/start use


Device Data table:
- User_ID + Device ID
- Device type
- Data 

Supplmentary tables:

Roles:
- User_ID
- Role_ID

Role_Definition:
- Role_ID
- Role_Catagory
- Role_permissions


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
  git clone this project and git checkout Devices
  cd to device-flask-project directory and run the following command:
  python ask_input.py 
    test with any inputs you like
