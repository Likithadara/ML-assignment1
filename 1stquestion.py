import statistics 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() # sorting the ages list 
minimum_age = min(ages) # finding the min age of the list
print("the minimum age in the list is : ",  minimum_age) 
maximum_age = max(ages) # finding maximum age of the list
print(" maximum age in the list is :", maximum_age) 
ages.append(min(ages)) # adding the min age to the list
ages.append(max(ages)) # adding the max age to the list
print("the elements after adding the min and max ages:" , ages) 
# finding median of ages
ages_median = statistics. median (ages) 
print("the median of the ages is :", ages_median) 
# finding average of ages
ages_average = sum(ages)/len(ages) 
print ("the  average of the ages is :", ages_average) # printing the average of the ages

ages_range = (max(ages) - min(ages)) # finding range of ages list
print("the range of the ages :", ages_range)   #printing the rangee of ages   