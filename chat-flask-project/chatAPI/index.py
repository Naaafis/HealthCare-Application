import json

from flask import Flask, jsonify, request
app = Flask(__name__)

message_collection = [
    
    {'sender': 'sender_name', 'recipient': 'recipient_name', 'message': 'message_body'}
    
]

def check_message(inp): 
    #this function just makes sure that the body of a message is is a string
    recipient_name = inp['recipient']
    sender_name = inp['sender']
    message = inp['message']
    
    if not isinstance(recipient_name, str):
        #tell user to enter valid id for recipient
        return "Please provide a string for the name of the recipient"
    
    if not isinstance(sender_name, str):
        #tell user to enter valid id for recipient
        return "Please provide a string for the name of the sender"
    
    if not isinstance(message, str):
        #tell user to reenter a valid message type
        return "Please provide string for the message body"
    
    return "Valid Message"

@app.route("/messages", methods=["GET"])
def get_all_messages():
    return jsonify(message_collection)

@app.route("/messages", methods=['POST'])
def add_device():
    new_message = request.get_json()
    if check_message(new_message) == "Valid Message":
        message_collection.append(request.get_json())
        return check_message(new_message)
    else: 
        return check_message(new_message)