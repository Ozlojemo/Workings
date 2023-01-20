#takes in an array of numbers and returns the average of all the numbers in the array.
my_array = [1,2,3]
total= 0
for i in my_array:
    total = total + i
avarage = total/len(my_array)
print(avarage)

