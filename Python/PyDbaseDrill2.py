import sqlite3

#creaating a temporary database in RAM
connection = sqlite3.connect(':memory:')

c.execute("DROP TABLE IF EXISTS People")

connection.close()

