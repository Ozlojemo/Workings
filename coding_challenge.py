# Coding Challenge: Regular Expressions in Python
# Objective:
# To understand and implement regular expressions in Python to match and extract specific patterns from a given string.
# Instructions:
# Use the re module in Python to implement regular expressions
# Write a function called extract_phone_numbers(string) that takes in a string and returns a list of all the phone numbers present in the string in the format (XXX) XXX-XXXX
# Write a function called extract_email_addresses(string) that takes in a string and returns a list of all the email addresses present in the string.
# Write a function called replace_email_addresses(string, replacement) that takes in a string and a replacement string, and replaces all email addresses in the given string with the replacement string.
# Use the provided test cases to test your functions

import re

test_string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"

# Function for extracting list of phone numbers from a string 
#  Got the regular expression from: https://stackoverflow.com/questions/37393480/python-regex-to-extract-phone-numbers-from-string
def extract_phone_numbers(random_string):
    return re.findall(r'[\+\(]?[1-9][\d .\-\(\)]{8,}[\d]', random_string)
    
# Function for extracting list of email addresses from a string
# Got the regular expression from: https://stackoverflow.com/questions/58749126/a-function-that-returns-email-addresses-from-a-list-of-strings-in-python
def extract_email_addresses(random_string):
    return re.findall(r'[\w\.-]+@[\w\.-]+', random_string)

# Function for replacing email addresses in a given string with a replacement string
def replace_email_addresses(random_string, replacement):
    email_list = extract_email_addresses(random_string)
    new_string = ""
    for email in email_list:
        new_string += random_string.replace(email, replacement)
    return new_string

print(extract_phone_numbers(test_string))
print(extract_email_addresses(test_string))
print(replace_email_addresses(test_string, "REPLACED"))