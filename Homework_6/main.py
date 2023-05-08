# Завдання 1:
a = []
for i in range(5):
    q = int(input(f'Введіть 5 чисел для списку {i+1} :'))
    a.append(q)
print(a)

# Завдання 2:
a = [1, 2, 3, 4, 5]
a.pop()
print(a)

# Завдання 3:
a = []
for i in range(10):
    q = int(input(f'Введіть число {i+1}:  '))
    a.append(q)
n = int(input('Введіть число, яке потрібно знайти :'))
count = 0
for q in a:
    if q == n:
        count += 1
print('число ', n, ' повторюється ', count, ' разів у списку')

# Завдання 4:
n = int(input('Введіть кількість чисел, які ви хочете зберегти в рядку:  '))
a = []
for i in range(n):
    q = int(input(f'Які числа ви хочете зберегти {i+1} : '))
    a.append(q)
a.reverse()
print('Ось ваш список : \n', a)

# Завдання 5:
a = []
c = []
for i in range(5):
    q = int(input(f'Введіть 5 чисел для списку {i+1}:  '))
    a.append(q)
print('Список А', a)
for q in a:
    if q > 5:
        c.append(q)
print('Список С', c)

# Завдання 6:
n = int(input('скільки чисел будемо записувати : '))
a = []
for i in range(n):
    num = int(input(f'Введіть числo {i+1}: '))
    a.append(num)
min_num = a[0]
max_num = a[0]
for num in a:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print(f'Мінімальне число = {min_num}')
print(f'Максимальне число =  {max_num}')

# Завдання 7:
text = input('Введіть текст: ')
symbol = 0
for i in text:
    if i.isdigit():
        symbol += 1
print(f'Кількість цифр у тексті : {symbol} ')





