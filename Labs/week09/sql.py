import mysql.connector
# Set up the db connection
db = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="datarepresentation"
)

# The cursor will hold the SQL comand
cursor = db.cursor()

# Insertting in to the database
# Split out the text from the values
# to avoid SQL injection
sql = "insert into student (firstname, age) values (%s,%s)"
# values
values = ("Mary", 21)

# Execute the command
cursor.execute(sql, values)

# Commit the changes to mySQL
db.commit()


# Get data from the database
cursor = db.cursor()

# write the statement
sql = "select * from student where id = %s"
# Populate the values
values = (1,)
# Execute the statement
cursor.execute(sql, values)

# Collect the result
result = cursor.fetchall() # can also use fetchOne()

# print out to screen all results
for x in result:
    print(x)
