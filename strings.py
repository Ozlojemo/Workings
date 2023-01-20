
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