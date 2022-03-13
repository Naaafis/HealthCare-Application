import user_chat as uc

def test_send_message():
    test_dict = {'sender': 'sender_name', 'recipient': 'recipient_name', 'message': 'message_body'}
    func_dict = uc.send_message('sender_name', 'recipient_name', 'message_body')
    assert test_dict['sender'] == func_dict['sender'], "Failed to compile sender name"
    assert test_dict['recipient'] == func_dict['recipient'], "Failed to compile recipient name"
    assert test_dict['message'] == func_dict['message'], "Failed to compile message"
   
def test_check_message(): 
    func_dict = uc.send_message('sender_name', 'recipient_name', 'message_body')
    test = uc.check_message(func_dict)
    assert test == "Valid Message", "Failed to validate message when all fields are valid"
    
    func_dict = uc.send_message(12, 'recipient_name', 'message_body')
    test = uc.check_message(func_dict)
    assert test == "Please provide a string for the name of the sender", "Failed to validate message when sender_name is in wrong format"
    
    func_dict = uc.send_message('sender_name', 12, 'message_body')
    test = uc.check_message(func_dict)
    assert test == "Please provide a string for the name of the recipient", "Failed to validate message when recipient_name is in wrong format"
    
    func_dict = uc.send_message('sender_name', 'recipient_name', 12)
    test = uc.check_message(func_dict)
    assert test == "Please provide string for the message body", "Failed to validate message when message is in wrong format"
    
    