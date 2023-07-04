MongoDB: insert_one()  
fred = {
 "student_id" : (1007)
 "first_name" : "Fred"
}
students = db.students
fred_student_id = students.insert_one(fred).inserted_id
 
print(fred_student_id)
 
ed = {
 "student_id"=(1008)
 "first_name"="ed"
 
students = db.students
ed_student_id = students.insert_one(ed).inserted_id
} 

Richard = {
 "student_id" = (1009)
 "student_name" = "Richard"
 
students = db.students
Richard = students.insert_one(Richard).inserted_id
}