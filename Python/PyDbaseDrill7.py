import sqlite3

rosterValues = (
    ('Jean-Baptiste Zorg', 'Human', 122),

    ('Korben Dallas', 'Meat Popsicle', 100),

    ("Ak'not", "Mangalore", -5)

)


with sqlite3.connect(":memory:") as connection:
        c = connection.cursor()

        c.execute("DROP TABLE IF EXISTS Roster")

        c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

        c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", rosterValues)

        # Update Korben Dallas to Human
        c.execute("UPDATE Roster SET Species=? WHERE Name=?",
                  ('Human', 'Korben Dallas'))

        c.execute("SELECT * FROM Roster")

        """for row in c.fetchall():
                  print row"""

        c.execute("SELECT Name, IQ FROM Roster")

        for row in c.fetchall():
                  print row
