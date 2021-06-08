# fruits = ['apple', 'banana', 'pineapple','123456789012']
#
# right_offset = len(max(fruits, key=len))
# print(right_offset)

# list_a = [1, 2, 3, 4, 5, 6]
#
# for a in list_a[:]:
#     print(a)
#     list_a.remove(a)
# print('end result for list_a: ', list_a)
import random

# elem_count = int(input('enter some number'))
# rand_list = []
#
# for _ in range(elem_count):
#     rand_list.append(random.randint(-100, 100))
# print(rand_list)

# a = [1, 2, 1, 3, 1, 4, 2, 5]
#
# first_a = list(set(a))
# print(first_a)
#
# second_a = list()
# for elem in a:
#     if a.count(elem) == 1:
#         second_a.append(elem)
#
# print(second_a)

# print(max('aaa', 'bb', 'z', 'xx', key=len))
#
# print(round(1.6213,3))
#
# def average(numbers):
#     count = len(numbers)
#     all_sum = sum(numbers)
#     print(round(all_sum/count,2))
#
# average([1,2,3,4,4,5,6,7,8,9,10])

# def func(name, **kwargs):
#     print(name, kwargs)
#
#
# func("ilya", surname='kamardin', age=32, flat=160.5)

# names = ['ilya', 'racheli', 'ely']
# age = (32, 31, 76)
#
# # for name, age in zip(names, age):
# #     print(name, age)
# print(list(zip(names, age)))
# print(dict(zip(names, age)))

# def my_pow(x):
#     return x ** 2
#
#
data = [-2, -10, 6, 19]

# result = []
#
# for num in data:
#     result.append(my_pow(num))
# print(result)
#
# result_1 = list(map(my_pow, data))
# print(result_1)


# def my_filter(x):
#     return x > 0
#
#
# result = list(filter(my_filter, data))
# print(result)

# result = list(map(lambda x: x ** 2, data))
# print(result)

# result = list(filter(lambda x: x > 0, data))
# print(result)

