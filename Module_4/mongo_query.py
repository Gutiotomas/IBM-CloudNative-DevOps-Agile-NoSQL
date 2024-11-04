from pymongo import MongoClient
user = 'tgutierrez'
password = 'Tg050801' # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXCERCISE - 2
host='mongo'
#create the connection url
connecturl = "mongodb+srv://{}:{}@db1.8qhzp.mongodb.net/?retryWrites=true&w=majority".format(user, password)

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select the 'training' database 

db = connection.training

# select the 'python' collection 

collection = db.python

# create a sample document

doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases"}

# insert a sample document

print("Inserting a document into collection.")
db.collection.insert_one(doc)

# query for all documents in 'training' database and 'python' collection

docs = db.collection.find()

print("Printing the documents in the collection.")

for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
connection.close()