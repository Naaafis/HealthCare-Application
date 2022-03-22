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


------------------------------------------------------------------------------------------------
## Processing Design

How many processes can be handled at the same time?
- However many workers I inialize to handle tasks, which is of course CPU and Memory Bound. This is handled in line 13,14 and 37 of index.py. In stead of viweing the queues with "rq worker", I would have to personally create Worker threads in the code, and the Queue that is displayed below would exist for each individual worker. The enqueing process would be running inside a while loop that consistently adds jobs to the queue of the smallest size, or use a tie breaker when there are multiple with the same sized queue. This process will be implemented when voice transcriber module is being completed. For now I have a working queue able to handle tasks as they come in one at a time. The simultaneous section still requires more work. 

- This process of creating multiple workers is ultimately utilizing multiple processes as the CPU of the server is what eventually ends up splitting its memory to handle multiple owrkers. Based on the load required for a voice transcriber, and the limitations of the t2.micro EC2 instance, I will implement 6 workers for a total of 6 API calls to be able to run simultaneously.

To handle the process of creating multiple workers, I can utilize the following source:
- https://python-rq.org/docs/workers/

Another option to use supervisor for multiprocessing in Redis: (first option is better and easier to implement)
- https://developpaper.com/supervisor-managing-redis-process-methodology-tutorial/



## Threading-flask

Sample application that simulates a delay and runs a background_task. The process of spinning up the sample API is by changing to threading-flask directory and running:
- pip install pipenv 
- pipenv --three
- pipenv install flask
- ./bootstrap.sh

The process of running redis server on macbooks:
- brew install redix
- brew services start redis
- rq worker

Below is examples of me sending multiple requests to the API server, and the API server utilizes a queue hosted by a redis brocker to handle all the requests in the background. Thats why the responses are served instantly even though the requests are all sent at the same time. The tasks are handled in the background by utilizing jobs and queues. To check the speed, go to the ip address where the API is running and after the "/" add "/task?n=N" where you replace "N" with any number to differentiate between requests. Although the background task is not returned instantly, the job ID is served instantly to show low latency in serving API response. The background task takes longer to complete but is handled sequentially and automatically. 

Incoming API requests:
![Image](./images/sending_requests.png)

Redis Queue Worker handling jobs and assinging IDs:
![Image](./images/handling_requests.png)