sisters=('deepthi','mini','lilly','lally') # sisters tuple 
brothers=('sai','deepak') # brothers tuple 
siblings=brothers+sisters  # combining both the tuples 
print(siblings) # printing number of siblings
length = len(siblings)
print('no of siblings are: ', length)
new_list = list(siblings)
#print("new_list")
new_list.append('raju') # adding father name to the list
new_list.append ('rajitha') # adding mother name to the list
new_tuple = tuple(new_list) # created new tuple to convert the list to tuple
family_members = new_tuple # assigning value in tuple to family_member varibale 
print(family_members) #printing family members 