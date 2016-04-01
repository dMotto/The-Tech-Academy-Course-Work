import sqlite3

#Setting up the database
connection = sqlite3.connect("test_database.db")
#connection = sqlite3.connect(':memory;')

#Communicating across the connection
c = connection.cursor()

#Creating table
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

#Inserting data into table
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

connection.commit()

connection.close()
