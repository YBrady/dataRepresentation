import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = ""
)
mycursor = mydb.cursor()
sql = "show databases"
mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
    print(x)
