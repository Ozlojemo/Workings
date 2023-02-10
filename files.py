
# file= open("Words.txt", "r")
# print(file.read ())

#Return first 5 characters

# file= open("Words.txt", "r")
# print(file.read(5))

#Read lines

# file= open("Words.txt", "r")
# print(file.readline())
# print(file.readline())

# file= open("Words.txt", "r")
# for arching in file:
#     print(arching)
    
# file= open("Words.txt", "r")
# count= 0
# for line in file:
#     count= count+ 1
#     print("line count", count)
        
file= open("Words.txt", "r")
input= file.read()
print(len(input))
print(input[:20])
    