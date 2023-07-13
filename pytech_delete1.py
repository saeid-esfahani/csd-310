""" import statements """
from pymongo import MongoClient
 
url = "mongodb+srv://admin:admin@cluster0.qiaw6a2.mongodb.net/"
client = MongoClient(url)
db = client.pytech
students = db.students

# find all students in the collection 
student_list = students.find({})

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
added_doc = {
    "student_id": "1010",
    "first_name": "saeid",
    "last_name": "esfahani"
}
added_doc_id = students.insert_one(added_doc).inserted_id

#finding inserted doc
student_added_doc = students.find_one({"student_id": "1010"})

#deleting 1010
deleted_student_added_doc = students.delete_one({"student_id": "1010"})

 
new_student_list = students.find({})

#printing documents with deleted info again
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

