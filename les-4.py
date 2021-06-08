# a = [1, 2, 3, 4, 5, 6]
#
# for number in a.copy():
#     print(number)
#     a.remove(number)
# print(a)

# b = a.copy()
# b.append(123)
# print(a)
# import copy
#
# a = [1, 2, 3, [100]]
# b = copy.deepcopy(a)
# b[3].append(200)
# print(a)
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for line in matrix:
#     for number in line:
#         print(number)
#
# matrix[2][2] = 11
# print(matrix[2][2])

# name = input("name\n")
# print(name or 'guest')

#
# age = int(input('Age = '))
# print('welcome' if age >= 18 else 'No Access')


# def admin():
#     print("I amdin")
#
#
# login = input('login: ')
#
# admin() if login == 'admin' else print('hello ' + login)

# a = 10
# b = 10
# b += 1
# print(a is b)

# result = []
# for i in range(10):
#     result.append(i)

# result = [i for i in range(10)]
# print(result)

# keys = 'qwerty'
# values = (1, 2, 3, 4, 5, 6)
#
# if len(keys) == len(values):
#     my_dict = {key: value * 2 for key, value in zip(keys, values)}
#     print(my_dict)

# a = [1]
# try:
#     b = a[0]
# except IndexError:
#     print('wrong index')


# a = []
# try:
#     b = a[0]
# except Exception as e:
#     print(e.__class__)


# try:
#     age = int(input('age = '))
# except :
#     print('abc')

