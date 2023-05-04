import math
print("Привіт, давай вирахуємо площу трикутника")
a = float(input('Сторона A : '))
b = float(input('Сторона B : '))
c = float(input('Сторона C : '))
# Визначимо периметр трикутника
p = (a + b + c) / 2
# Визначимо площу трикутника
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f'answer is {s}')
