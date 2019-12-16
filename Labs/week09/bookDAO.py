import mysql.connector
import dbconfig as cfg

class BookDAO:
    # Setting the database to null at the start
    db = ""
    def __init__(self):
        # Make the connection - here we are specifying the datatbase (datarepresentation)
        self.db = mysql.connector.connect(
            host=cfg.mysql["host"],
            user=cfg.mysql["user"],
            password=cfg.mysql["password"],
            database=cfg.mysql["database"]
        )

    # The function to create a student (a row in a database table) - 
    # expecting values to be written in when this function is called
    def create(self, values):
        # Create the cursor
        cursor = self.db.cursor()
        # The SQL statement - without actual values
        sql = "insert into book (title, author, price) values (%s,%s, %s)"
        # Putting the SQL statement and the values together for execution
        cursor.execute(sql, values)
        # Commit changes to db
        self.db.commit()
        # Return the id number of the new person created
        return cursor.lastrowid

    # Function to return all rows
    def getAll(self):
        # Create the cursor
        cursor = self.db.cursor()
        # Make the select statment
        sql = "select * from book"
        # Execute the statement
        cursor.execute(sql)
        # Write the results to the results variable
        results = cursor.fetchall()
        # Create a blank array to house the converted results
        returnArray = []
        # One by one, for the results
        for result in results:
            # Turn each result into a dictionary object
            returnArray.append(self.convertToDictionary(result))
        # Return the converted results
        return returnArray

    # Find an item by their id number
    def findByID(self, id):
        # Create the cursor
        cursor = self.db.cursor()
        # The SQL statement
        sql = "select * from book where id = %s"
        # Add the values (has to be in brackets with a comma as a tuple is expected)
        values = (id,)
        # Perform the SQL statement
        cursor.execute(sql, values)
        # Collect the results - fetchOne = 1 result
        result = cursor.fetchone()
        # Return the dictionary converted result
        return self.convertToDictionary(result)

    # Function to update a row - assumed new values are entered when calling the function
    def update(self, values):
        # Create the cursor
        cursor = self.db.cursor()
        # Write the SQL statement without the values
        sql = "update book set title= %s, author = %s, price=%s where id = %s"
        # Perform the update
        cursor.execute(sql, values)
        # Commit to database
        self.db.commit()

    # Function to delete a row - assuming id is enered when function is called
    def delete(self, id):
        # Create the cursror
        cursor = self.db.cursor()
        # Make the SQL statement without values
        sql = "delete from book where id = %s"
        # Add the values
        values = (id,)
        # Execute the SQL statement
        cursor.execute(sql, values)
        # Commit the changes
        self.db.commit()
        # Print as a feedback that the code has executed
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

bookDAO = BookDAO()
