# Import mySQL connector python package
import mysql.connector
# Set up the connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datarepresentation"
)

# Create the cursor
cursor = db.cursor()
# The mySQL select - take away the where id bit if you want to return all rows
sql = "select * from student"# where id = %s"
# This is needed for where the id = 
# Comma needed as it is a tuple
values = (1,)
# Do the select statement
cursor.execute(sql)#, values)
# Save the result into the result variable
result = cursor.fetchall()
# For all the results found
for x in result:
    # Print out 
    print(x)
