# 1
my_file = 'pancakes.txt'
digits = []
with open(my_file, 'r') as file:
    for line in file:
        for i in line:
            if i.isdigit():
                digits.append(int(i))
print(digits)

# 2
f = open('data.txt', 'w')
a = input('Введіть текст: ')
f.write(a)

# 3
f = open('numbers.txt', 'w')
a = int(input('Скільки чисел ви бажаєте записати: '))
n = int(input('Запишіть ці числа: '))
f.write(n)

# 4
import random
file = 'random_numbers.txt'
with open(file, 'w') as f:
    for i in range(100):
        random_number = str(random.randint(1, 1000))
        f.write(random_number + '\n')

# 5
a = 'pancakes.txt'
words = 0
with open(a, 'r') as file:
    for i in file:
        word = i.split()
        words += len(word)
print('Кількість слів у файлі :', words)

# 6
with open('numbers_6.txt', 'r') as file:
    numbers = file.read().split()
    summ = 0
for num in numbers:
    summ += int(num)
print('Сумма чисел у тексті :', summ)

# 7
from collections import Counter

with open('text.txt', 'r') as file:
    words = file.read().split()
    word_counts = Counter(words)
    top_words = word_counts.most_common(5)
for word, count in top_words:
    print(f'{word} - {count} разів' )















