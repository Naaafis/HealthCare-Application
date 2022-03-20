#Source: https://pythonise.com/series/learning-flask/flask-rq-task-queue

from flask import Flask, request
import redis 
from rq import Queue

import time

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection = r)

def background_task(n):

    """ Function that returns len(n) and simulates a delay """

    delay = 2

    print("Task running")
    print(f"Simulating a {delay} second delay")

    time.sleep(delay)

    print(len(n))
    print("Task complete")

    return len(n)

@app.route("/task")
def index():

    if request.args.get("n"):

        job = q.enqueue(background_task, request.args.get("n"))

        return f"Task ({job.id}) added to queue at {job.enqueued_at}"

    return "No value for count provided"

