# Числа які діляться на 3:
N = int(input("Введіть число : "))
i = 0
while i <= N:
    if i % 3 == 0:
        print(i)
    i += 1

#Числа, які діляться на 3 без залишку:
N = int(input("Введіть число : "))
i = 0
sum = 0
while i <= N:
    if i % 3 == 0:
        sum += i
    i += 1
print("Сумма чисел які діляться на 3 без залишку:  ", sum)
