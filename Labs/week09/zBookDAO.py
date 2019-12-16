import mysql.connector

class zBookDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            # user="datarep", # this is the user name on my mac
            # passwd="password" # for my mac
            database="datarepresentation"
        )


    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into book (title, author, price) values (%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from book"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from book where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result


    def update(self, values):
        cursor = self.db.cursor()
        sql = "update book set title= %s, author=%s, price=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()


    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from book where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")

    # Function to convert the return values to dictionary items
    def convertToDictionary(self, result):
        # Create the column names
        colnames = ["id", "Title", "Author", "Price"]
        item = {}  # blank dictionary object
        
        # Execute only if the result has something in it
        if result:
            # For every column name
            for i, colName in enumerate(colnames):
                # Match the column name with the result based on location in tuple
                item[colName] = result[i]
        # Return the dictionary-ise item
        return item

bookDAO = zBookDAO()
