# HealthCare-Application

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
- Device name
- Device ID
- Device MAC Addr
- User it belongs to ID
- User it was assigned by ID
- Firmware version
- Software version
- Date of Purchase/start use


Device Data table:
- User_ID + Device ID
- Data collected time
- Data 

Supplmentary tables:

Roles:
- User_ID
- Role_ID

Role_Definition:
- Role_ID
- Role_Catagory
- Role_permissions

Chat Tables: 
- Senders and Recipients have unique IDs that will be unified to search for messages
- Messages and message IDs 


------------------------------------------------------------------------------------------------
ChatAPI abilities:
API is capable of sending and viewing messages between two users. The POST calls are used to post messages with sender and recipient specified, while the id used to store messages common senders and recipients are created by combining the name of the sender and recipient and alphabetizing the combination. The GET calls require specification of 'sender' and 'recipient' in order to get a collection of all messages sent between the users. 

To send a message the following parameters need to be specified:
sender_name, recipient_name, message

To view messages between two users the following parameters need to be specified: 
sender_name, recipient_name

ChatAPI use instrucitons:

To deploy API, cd into chat-flask-project and run the following commands:
pip install pipenv
pipenv --three
pipenv install flask
./bootstrap.sh

take note of the http link running the API

use POST calls along with the following parameters for json requests to send messages:
{sender: *string*, recipient: *string*, message: *string*}


For the purposes of this application, I will deploy the API myself on an EC2 instance

------------------------------------------------------------------------------------------------
Database for Chat decision purposes:

- Need something lightweight to be able to constantly update the database when new messages are received
- Must follow all of ACID properties
- Dont really need PRIMARY and FOREIGN keys as there is no need for object relational mapping when messages are only relevant to one key
- Need the CR part of CRUD operations to be able to create and retrieve messages, might even need to update and delete messages 
- The Key would simply be a ID created for the tuple of the sender and recipient pair 
- Just need one collection called messages, it'll hold each document as messaging sessions between two users
- Easy to scale documents by nesting it with new messages
- Hence I will be using MongoDB

------------------------------------------------------------------------------------------------
To use mongoDB: 
Run the following commands:

On MacOS:
brew services start mongodb-community@5.0
mongosh

I will personally deploy a database for the purposes of testing
