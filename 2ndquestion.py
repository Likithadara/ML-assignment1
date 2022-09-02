dog= {} # creating empty dict
#assigning keys and values 
dog = {"name": "spunky","color": "brown","breed": "germanshapad", "legs": "large", "age" : "1 year"}
print("dog dict :", dog)
#creating a student deict and assigning valyes to the dic
student ={"first_name": "deepthi","last_name": "dara","gender":"female","age":"23","marital status":"single"
,"skills":["java", "python"], "country":"india", "city":"hyderabad","address":"uppal"}
print("student dict :",student)
length_student = len(student)
print("the length of the student dictionary is :", len(student))
 # getting skill type in  list format
print("skills and type of skill is :",type(student['skills']))
#adding more skill values
student['skills'] ={" dotnet "," angularJs"}
print("", student["skills"])
# printing dictionary keys as list
print(student.keys())
# printing dictionary values as list
print(student.values())
