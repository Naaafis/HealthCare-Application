import user_chat as uc
import requests 
import json 

def ask_message_info():
    sender = input("who is the sender of this message: ")
    receiver = input("who is hte recipient of this message: ")
    message = input("what is the message you want to send: ")
    packaged = uc.send_message(sender, receiver, message)
    return packaged

def ask_users(): 
    sender = input("who is the sender of this message: ")
    receiver = input("who is hte recipient of this message: ")
    packaged = uc.users(sender, receiver)
    return packaged

def main(): 
    url = "http://54.66.50.61:5000/"
    
    while(1):
        t = input("enter 's' to send a message and 'v' to view messages: ")
        if t == 's':
            url1 = url + "messages"
            m = ask_message_info()
            req = requests.post(url1, json=m)
            print(req.text)
            
        if t == 'v': 
            url2 = url + "messages"
            u = ask_users()
            req = requests.get(url2, json=u)
            print(req.text)
            
            
if __name__ == "__main__":
    main()