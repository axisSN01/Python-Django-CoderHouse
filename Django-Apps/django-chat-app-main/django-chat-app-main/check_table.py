import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('db.sqlite3')

# Create a cursor object
cursor = connection.cursor()

# Execute a sample query
cursor.execute("SELECT * FROM django_migrations")

# Fetch all rows from the query result
rows = cursor.fetchall()

# Process the fetched rows
for row in rows:
    print(row)

# Execute a sample query
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all rows from the query result
rows = cursor.fetchall()

# Process the fetched rows
for row in rows:
    print(row)


while True:
    print("\n\nPress q + ENTER to exit\n")
    query = input("tip SQL Query: ")
    print()

    if query == "q":
        break

    try:
        cursor.execute(query)  
        # Fetch all rows from the query result
        rows = cursor.fetchall()
        # Process the fetched rows
        for row in rows:
            print(row)

    except Exception as myExc:
        print(myExc)


# Close the cursor and the database connection
cursor.close()
connection.close()

