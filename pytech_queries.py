
MongoDB: find()
docs = db.collection_name.find({})
 
for doc in docs:
 print(doc)
 
MongoDB: find_one()
doc = db.collection_name.find_one({“student_id”: “1007”})
 
print(doc[“student_id”])

MongoDB: find_one()
doc = db.collection_name.find_one({“student_id”: “1008”})
 
print(doc[“student_id”])
MongoDB: find_one()
doc = db.collection_name.find_one({“student_id”: “1009”})
 
print(doc[“student_id”])
