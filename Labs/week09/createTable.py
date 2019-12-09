# Import package for mySQL connections
import mysql.connector

# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datarepresentation"
)

# Create cursor
mycursor = mydb.cursor()

# Write SQL create statement 
sql ="CREATE TABLE student(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

# Execute the statement
mycursor.execute(sql)
