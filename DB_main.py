import mysql.connector
import time 
import datetime

ts=time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

#this portion is to test uploading a user to a database

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#########", #for the purposes of github, I will not include this in the commit 
  database="HealthcareApp"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (id, full_name, date_of_birth, address, primary_care_provider, insurance, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (1, "John", "January 2nd, 1998", "Highway 21", "Bilal MD", "HealthPlus", timestamp)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")