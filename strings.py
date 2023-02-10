
a= """ I was sitting, in the office, with Robert at 6am"""
print(a)

a= "Hello, world"
print(a[0])

for x in "banana":
    print(x)
    
a= "Hello, World"
print(len(a))

text= "The free things in life are free"
print("free" in text)
if "free" in text:
    print("Yes, free is present")
else:
    print("No, free is not present")

b= "Hello World"
print(b[2:5])
print(b[:5])
print(b[0:])
print(b[-5:-2])

a= "Hello, World"
print(a.upper())
print(a.lower())

#Removing White space
a=   "Hello, World"        
print(a.strip())
#Replacing String
a="Hello, World"
print(a.replace("H", ("J")))

#Spliing a string
a= "Hello, World"
print(a.split(","))

#String Concatenation
a= "Hello"
b= "World"
c= a +" "+ b
print(c)

#String Format
# age= 30
# txt= "My name is James Osolo,I am" + age
# print(txt)= Error must be strings not integer

age= 30
txt= "My name is James Osolo,I am {}"
print(txt.format(age))

Quantity= 10
Item= 500
Price= 100

myorder= "I want {} pieces of items {} for {} dollars"
print(myorder.format(Quantity,Item,Price))

#Escape characters

# txt = "We are the so-called "Vikings" from the north."
# print(txt) Error-Not allowed

txt = "We are the so-called \"Vikings\" from the north."
print(txt)