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
sql = "insert into student (name, age) values (%s,%s)"
values = ("Mary", 21)
cursor.execute(sql, values)
db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
