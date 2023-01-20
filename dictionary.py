# #key value pairs
# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(thisdict)
# print(thisdict["brand"])
# print(thisdict["year"])

def parse_file (filepath):
    with open(filepath, "r") as file: 
        file_contents=file.read().split("\n")
        list_of_sublist= []
        for i in file_contents: 
            name=i.split(",")[0]
            address= i.split(",")[1]+ ","+i.split(",")[2]
            sublist= [name, address]
            list_of_sublist.append (sublist)   
        address_book= {}
        for i in list_of_sublist:
            my_key= i[0]
            my_value=i[1]
            address_book[my_key]= my_value
        return address_book
returned_adress_book= parse_file("Dictonary file.txt")
print(returned_adress_book)