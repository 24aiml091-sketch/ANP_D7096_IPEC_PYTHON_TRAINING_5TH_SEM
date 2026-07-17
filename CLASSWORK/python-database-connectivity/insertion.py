
import mysql.connector

# Establish connection
data_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sanjay",
    database="studentM"
)
print("Database connection estabilished")
cursorobj = data_connection.cursor()
sql_query = 'insert into student values (%s,%s,%s,%s)'
stdid ='std101'
stdname = 'anil'
standard = '10th'
age = 20
value = (stdid ,stdname,standard,age)
cursorobj.execute(sql_query,value)
data_connection.commit()
if(cursorobj.rowcount > 0):
    print("insert successfully")
else:
    print("data not inserted")
cursorobj.close()
data_connection.close()