# name_and_lastname = "ilya" + "kamardin"
# print(name_and_lastname[-1])
# print(name_and_lastname[0:4])
# print(name_and_lastname[:4])
# print(name_and_lastname[4:])
# print(name_and_lastname[::-1]) #if we need to write some word in revers we can use this [::-1]
# [from : to(not include) : step]

# if we need for example check if we have a email we need confirm we have a @ we can use this
# email = "ilya.ccnp@gmail.com"
# index = email.find("@")
# print(index)
# print(email[:index])
# print(email[index+1:]) # if ew need to tack the word until @
#
name = 'iLYa KamaRdin'

# print(name.lower())        # ilya kamardin
# print(name.upper())        # ILYA KAMARDIN
# print(name.capitalize())   # Ilya kamardin
# print(name.title())        # Ilya Kamardin

# print(len(name))           # 13

# print(name.count('a'))     # 3   # its count how many time our sequence apear
# print(name.lower().count('a')) for count no meter if its upper case or lower case

print(name.split())  # ['iLYa', 'KamaRdin']
print(name.split("a"))  # ['iLY', ' K', 'm', 'Rdin']

# list
humans = ["ilya", "racheli", "dalya", "ely"]

print(humans)  # ['ilya', 'racheli', 'dalya', 'ely']
humans.append(10)
print(humans)  # ['ilya', 'racheli', 'dalya', 'ely', 10]
humans.insert(2, 'lena')
print(humans)  # ['ilya', 'racheli', 'lena', 'dalya', 'ely', 10]
print(humans.index(10))  # 5
print(humans.index('ilya'))  # 0
humans.remove('dalya')  # ['ilya', 'racheli', 'lena', 'ely', 10]
print(humans)

# humans.remove(10) # !if the value not exist its throw error
# print(humans)
# print(humans.pop())#10
# print(humans.pop())#ely
# print(humans.pop())#lena
# print(humans)#['ilya', 'racheli']
print(humans.pop(-1))  # the default is -1  # we can write some number in () and it's pop the number

# if we need check if some name exist in our string we can use :
print('ilya' in humans)  # True
print('il' in humans)  # False

# if we need to tuch some inside element for example :
x = [1, 2, 3, ['ilya', 'rhcheli']]
print(x[3][0])  # ilya

# if we need to copy tuple we can do this :
humans_tuple = (1, 2, 3, 4, 5)
humans_list = list(humans)

# we can use while iterator
x = 0
while x < len(humans):
    print(humans[x])
    x = x + 1

# we can do same thing with more efective loop his name for
for name in humans:
    print(name)

# for i in humans:
#     print(i)


# for i in range(10):
#     print(i)  # 0,1,2..9
#
# # we can use start and end
# for i in range(1, 10):
#     print(i)          # 1,2,3...9

person = {'name': 'ilya', 'age': 32, 'money': 100.0}
print(person['name']) #ilya
print(person['age']) #32
print(person['money']) #100.0
