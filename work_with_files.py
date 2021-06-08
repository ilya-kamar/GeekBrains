# file = open('some_file.txt')
# for line in file:
#     print(line, end='ilya')

# file = open('1.txt', 'a+', encoding='utf-8')
# file.write('\nmonday\n')
# file.seek(0)
# print(file.readlines())
# file.close()

with open('1.txt') as f:
    for line in f:
        print(line.strip())