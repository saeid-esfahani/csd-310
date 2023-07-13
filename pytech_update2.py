from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.qiaw6a2.mongodb.net/"
client = MongoClient(url)
db = client.pytech
# so far I have connected to the student database

students = db.students
student_list = students.find({})

#getting students info and finding them.

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "  First Name: " + doc["first_name"] + "  Last Name: " + doc["last_name"] + "\n")
"\n"
"\n"
#updating last names
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Mardani"}})
result = students.update_one({"student_id": "1008"}, {"$set": {"last_name": "habibi"}})
result = students.update_one({"student_id": "1009"}, {"$set": {"last_name": "Saberi"}})

MongoDB: find_one()
doc = db.collection_name.find_one({"student_id": "1007"})
 
# find the updated student document 
thorin = students.find_one({"student_id": "1007"})


print("  Student ID: " + thorin["student_id"] + "\n  First Name: " + thorin["first_name"] + "\n  Last Name: " + thorin["last_name"] + "\n")
