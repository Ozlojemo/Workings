#list

numbers = [1,2,3,4,5,6,7,8,9,10]

#tuply
words = ("hello", "world", "python", "coding", "bootcamp")
result = []
for x in range (0,10):
    result.append (numbers[x])
    if x <= 4 : 
        result.append(words[x])
print(result)
print(len(numbers))

#The sublist containing the values from index 2 to index 5
 
Sublist1 = result [2:5]
Sublist2 = result[-5:]
print("sublisti1", Sublist1)
print("sublisti2", Sublist2)
print("element at index 4: ", result[4])
print("last element", result[-1])
print(result.count("python")) 
if 3 in result:
    print("Yes three in result")
else:
    print("No three is not in result")
result.remove(3)
print(result)
result.insert(6,"programming")
print(result)
#print(result.sort()) #cannot run, result list has two different data type
#print(result.sort(reverse = True))
final_tuple= tuple(result)
print(final_tuple)