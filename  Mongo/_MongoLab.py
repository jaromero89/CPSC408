import pymongo

client = pymongo.MongoClient('mongodb+srv://5ec9df137040920ab3747796@cpsc408_MongoDB.gcp.mongodb.net/test?retryWrites=true&w=majority')

db = client.cpsc408
print(client.list_database_names())

students = db.Student

#insert Student by first name, lastname, major as well as courses
students.insert_one({ "FirstName": "James","LastName": "Romero",
                     "Major": ["CPSC"],"Courses": [ "CPSC 408", "CPSC 402" "CPSC 390", "CPSC 380" ] })

# Selects student based on the following criteria
for s in students.find({"Major" : "CPSC"}):
    print(s["FirstName", "LastName"])

# select document
for s in students.find():
    print(s)

print(client.list_database_names())