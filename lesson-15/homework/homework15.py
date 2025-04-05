# 1
import sqlite3
conn = sqlite3.connect("mydatabase.db")
cur = conn.cursor()
cur.execute("""create table Roster (Name text, Species text, Age integer)""")
conn.commit()
conn.close()

# 2
conn = sqlite3.connect("mydatabase.db")
cur = conn.cursor()
cur.execute("""
create table if not exists Roster (Name text, Species text, Age integer)""")
cur.execute("insert into Roster (Name, Species, Age) values ('Benjamin Sisko', 'Human', 40)")
cur.execute("insert into Roster (Name, Species, Age) values ('Jadzia Dax', 'Trill', 300)")
cur.execute("insert into Roster (Name, Species, Age) values ('Kira Nerys', 'Bajoran', 29)")
conn.commit()
conn.close()
print("Data is added to the table.")

# 3
conn = sqlite3.connect("mydatabase.db")
cur = conn.cursor()
cur.execute("update Roster set Name = 'Ezri Dax' where Name = 'Jadzia Dax'")
conn.commit()
conn.close()
print("updated")

# 4
conn = sqlite3.connect("mydatabase.db")
cur = conn.cursor()
cur.execute("select Name, Age from Roster where Species = 'Bajoran'")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
