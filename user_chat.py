
def send_message(sender_name, recipient_name, message): 
    #this funciton exists to return a tuple with the sender and recipient as part of the same key 
    #typically this would also need to have a timestamp, but we will use data base for that function
    Dict = {'sender': sender_name, 'recipient': recipient_name, 'message': message}
    return Dict

def users(sender_name, recipient_name): #this function is just there to get user messages
    Dict = {'sender': sender_name, 'recipient': recipient_name}
    return Dict

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

def check_users(inp): #this function just makes sure usernames are in the correct format
    recipient_name = inp['recipient']
    sender_name = inp['sender']
    
    if not isinstance(recipient_name, str):
        #tell user to enter valid id for recipient
        return "Please provide a string for the name of the recipient"
    
    if not isinstance(sender_name, str):
        #tell user to enter valid id for recipient
        return "Please provide a string for the name of the sender"
    
    return "Valid Message"