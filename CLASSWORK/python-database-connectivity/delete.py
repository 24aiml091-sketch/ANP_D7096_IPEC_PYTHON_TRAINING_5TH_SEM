import mysql.connector

# Establish connection
data_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sanjay",
    database="studentM"
)
print("Database connection estabilished")
# Create cursor object
cursor_obj = data_connection.cursor()

# Take Student ID as input
std_id = input("Enter Student ID to delete: ")

# Delete query
sql_query = "DELETE FROM student WHERE std_id = %s"

# Execute query
cursor_obj.execute(sql_query, (std_id,))

# Commit changes
data_connection.commit()

# Check if a record was deleted
if cursor_obj.rowcount > 0:
    print("Student record deleted successfully.")
else:
    print("No student found with the given ID.")

# Close connection
cursor_obj.close()
data_connection.close()