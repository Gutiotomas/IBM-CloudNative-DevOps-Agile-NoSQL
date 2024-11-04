from pymongo import MongoClient

# Define your user credentials
user = 'tgutierrez'
password = 'Tg050801'  # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXERCISE

# Create the connection URL for MongoDB Atlas
connecturl = "mongodb+srv://{}:{}@db1.8qhzp.mongodb.net/?retryWrites=true&w=majority".format(user, password)

# Connect to MongoDB server
print("Connecting to MongoDB server...")
connection = MongoClient(connecturl)

# Get database list
print("Getting list of databases...")
dbs = connection.list_database_names()

# Print the database names
for db in dbs:
    print(db)

print("Closing the connection to the MongoDB server...")

# Close the server connection
connection.close()
