# comments we can use 2 type of comments first is one line => #
''' second we can use the multiline comment'''
# Arithmetic operators in Python
# a//b  this is int devide

# a = 5.5
#
# list_example = [10, a, "yosi"]
# print(type(list_example))
# list_example.append(68.3)
#
# tuple_example = (10, a, "yosi")
# print(type(tuple_example))

# the diference between list and tuple the tuple we can't change its help for define some value that we not need to chane
# in the code for example if we need to define month of the year we not wont for some reason we change it


# dictionary
# dictionary_example = {'name': 'ilya', 'age': 32, "b.date": "19/12/1988"}
# print(dictionary_example)
# print(dictionary_example['age'])
# we can write every type of data in value or in the key

# print(5 > 1)
# print(type(5 < 1))
# print(5 == 1)
# print(5 >= 1)
# print(5 <= 1)
# print(5 != 1)

# bool    the 0 or empty string ''  mean this is False ather value is True

# number = int(input("enter some number: \n"))
# while number < 1 or number > 5:
#     number = int(input("you need enter number between 1 and 5\n"))

# we can write x+=1 its same  x = x + 1
x = 0
while x <= 10:
    x = x + 1
    
    if x == 10:
        break
    print(x)
else:
    print("end while")
