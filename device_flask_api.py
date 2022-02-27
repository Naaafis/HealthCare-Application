import register_device as rd
import collect_data as cd 
import ask_input as ai

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def get_input():
    # input_type = input("Enter 'r' for registration and 'c' for collection: ")
    # if input_type == 'r':
    #     return ai.ask_registration_input()
    # elif input_type == 'c':
    #     return ai.ask_collection_input()
    # else:
    #     return "Invalid Input"
    ai.ask_registration_input()

if __name__ == "__main__":
    app.run()