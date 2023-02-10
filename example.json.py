 

import json



Person= {"name":"John", "age": 30,"city":"New York", "hasChildren": False, "titles":["engineer", "programmer"]}

#convert into json

person_json= json.dumps(Person)
print(person_json)

with open("person.json", "w") as file:
    json.dump(person_json,file)