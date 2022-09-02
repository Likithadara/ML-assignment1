No_of_students = int(input("enter number of students")) 
weight_kgs = []
weight_lbs = []
print("enter weight of the studsent "+ str(No_of_students)+" students")
for  t in range(No_of_students):
    student_weight = int(input(str(t+1)+". student weight:")) #assigning the input to student_weight
    weight_lbs.append(student_weight) 
    # 1lbs=0.453kgs converting the lbs entered by the user to kgs by multiplying the weight with 0.453
    weight_kgs.append(float("{: .2f}" . format (student_weight * 0.453)))
print ("weight of student in lbs :", weight_lbs)
print("weight of student in kgs :", weight_kgs)

