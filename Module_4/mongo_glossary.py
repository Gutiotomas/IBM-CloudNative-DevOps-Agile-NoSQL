from pymongo import MongoClient
user = 'tgutierrez'
password = 'Tg050801' # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXCERCISE - 2
host='mongo'
#create the connection url
connecturl = "mongodb+srv://{}:{}@db1.8qhzp.mongodb.net/?retryWrites=true&w=majority".format(user, password)

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

db = connection.training

collection = db.mongodb_glossary

doc1 = {"database": "a database contains collections"}
doc2 = {"collection": "a collection stores the documents"}
doc3 = {"document": "a document contains the data in the form of key value pairs"}

print("Inserting documents into collection.")
db.collection.insert_one(doc1)
db.collection.insert_one(doc2)
db.collection.insert_one(doc3)


docs = db.collection.find()

print("Printing the documents in the collection.")

for document in docs:
    print(document)

print("Closing the connection.")
connection.close()