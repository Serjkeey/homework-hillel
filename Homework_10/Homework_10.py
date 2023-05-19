# 1
# my_file = 'pancakes.txt'
# digits = []
# with open(my_file, 'r') as file:
#     for line in file:
#         for i in line:
#             if i.isdigit():
#                 digits.append(int(i))
# print(digits)

# 2
# f = open('data.txt', 'w')
# a = input('Введіть текст: ')
# f.write(a)

# 3
# f = open('numbers.txt', 'w')
# a = int(input('Скільки чисел ви бажаєте записати: '))
# n = int(input('Запишіть ці числа: '))
# f.write(n)

# 4
# import random
# file = 'random_numbers.txt'
# with open(file, 'w') as f:
#     for i in range(100):
#         random_number = str(random.randint(1, 1000))
#         f.write(random_number + '\n')

# 5
a = open('pancakes.txt', 'r')
a.read()
print(len(a))

















