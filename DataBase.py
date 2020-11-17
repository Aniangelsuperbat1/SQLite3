import sqlite3

# Connects to database and creates and table
con = sqlite3.connect("MoorseCode.db")

# Create a Cursor
C = con.cursor()

# # Dont need after table is created
# C.execute("""CREATE TABLE MoorseCode (
#             Letter text,
#             Value text
#             )""")

# multiple_Elements = [("B", "-..."), ("C", "-.-."), ]

# Adds one value into table
# C.execute("INSERT INTO MoorseCode VALUES ('A', '.-')")

# Adds many values into the table
# C.executemany("INSERT INTO MoorseCode VALUES (?,?)", (multiple_Elements))

# Query the Database
# C.execute("SELECT * FROM MoorseCode")

# Searches through database for specifc elements
# C.execute("SELECT * FROM MoorseCode WHERE...")

# Both conditions have to be true in order to return a result (AND)
# One condition has to be true (OR)
# C.execute("SELECT * FROM MoorseCode WHERE ... LIKE... AND/OR...")

# Returns "auto complete" of likey canidates of your search
# C.execute("SELECT * FROM MoorseCode WHERE... LIKE...%")

# Prints hidden Rows. RowID.
# C.execute("SECLET rowid, * FROM MoorseCode")

# print(C.fetchall())

# updates records
# c.execute """UPDATE MoorseCode SET Letter/Value =...
#              WHERE rowid =...
# """

# Delete Records
# c.execute("DELETE from MoorseCode WHERE rowid/Letter/Value =..."")

# Delete Table
# # C.execute ("DROP TABLE MoorseCode")

# Prints data in whatever way you want it to
# C.execute("SECLET rowid, * FROM MoorseCode ORDER BY...")
# DESC: Descending order
#

# Limit: Return only a limited amount of results:
# C.execute("SECLET rowid, * FROM MoorseCode Limit (number)")

# Can print all items or make it a variable
# Elements = C.fetchall()

# for item in Elements:
#     print(item)

# Can play around with formatting. Index of items.
# for item in Elements:
#     print(item[0])

con.commit()

con.close()
