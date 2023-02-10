
import re

#Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#     print("Yes, we have a match")
# else:
#     print("No, we do not have a match")
    
# x = "My two favorite numbers are 19 and 42"
# y= re.findall("[0-9]+", x)                                                                                                                                                                                             
# print(y)

# The findall() Function

# txt = "The rain in Spain"
# x= re.findall("ai", txt)
# print(x)

# # Return an empty list if no match was found:
# txt= "The rain in Spain"
# x= re.findall("Door", txt)
# print(x)

# The search() Function

#Search for the first white-space character in the string:
# txt= "The rain in Spain"
# x= re.search("\s", txt)
# print("The first white space character is located in:",x.start())

# The split() Function

# txt = "The rain in Spain"
# x= re.split("\s", txt )
# print(x)

# You can control the number of occurrences by specifying the maxsplit parameter:
# Split the string only at the first occurrence:

txt = "The rain in Spain"
x= re.split("\s", txt,1)
print(x)

# The sub() Function
# Replace every white-space character with the number 9:

# txt = "The rain in Spain"
# x= re.sub("\s", "9", txt)
# print(x)

# Replace the first 2 occurrences with digit 9

# txt = "The rain in Spain"
# x= re.sub("\s", "9",txt, 2)
# print(x)

# Match Object
# search that will return a Match Object:

# txt = "The rain in Spain"
# x= re.search("ai", txt)
# print(x)

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain"
x= re.search(r"\bS\w+", txt)
print(x.span())

# Print the string passed into the function:
#The string property returns the search string:

txt = "The rain in Spain"
x=re.search(r"\bS\w+", txt)
print(x.string)

# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":

txt = "The rain in Spain"
x=re.search(r"\bS\w+", txt)
print(x.group())