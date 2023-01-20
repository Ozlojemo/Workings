import math
#s is a monty python 
s = "monty python"
print(s[0:4])
print(s[5:10])
print(s[6:20])
print(s[:])
# Area of a circle
#A = πr²
radius=40
area = math.pi * math.pow(radius,2)
print(f"area:{area}")
a= "Hello "
b= a + "there"
print(b)
fruit = "banana"
"n" in fruit 


vowels = ["a","e","i", "o", "u"]
fruit = "banana"
count = 0
for letter in fruit :
    if (letter in vowels):
        count = count + 1 
        print(letter)
print (count)              

fruit = "banana"
print (len(fruit))


#files
 
# stuff = "hello\nworld!"
# print(stuff)

# fhand = open("mbox.txt")
# count   = 0
# for line in fhand: 
#     count= count +1 
# print ( "line count: ",count)    

Reports = open ("Dec Upload.txt")
count = 0
for line in Reports:
    count= count +1
print ("line count:", count)

# reports = open("Dec Upload.txt")
# input = reports. read ()
# print(len(input))
# print(input[:20])

# reports = open ("Dec Upload. txt")
# for line in reports :
#     if line. startswith ("9060"): 
    
#palindrome
def isPalindrome(my_string): 
    return my_string == my_string[::-1]
def fileInput(filename):
    for line in open(filename):
        if isPalindrome(line.strip()):
            print(line.strip(), " is a palindrome.")
fileInput("words.txt") 
    