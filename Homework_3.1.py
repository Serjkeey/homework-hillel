#Числа, які діляться на 3:
enter_number = int(input('Введіть число:  '))
for number in range(enter_number + 1):
    if number % 3 == 0:
        print(number)

#Числа, які діляться на 3 без залишку:
enter_number = int(input('Введіть число:  '))
summ = 0
for number in range(enter_number + 1):
    if number % 3 == 0:
        summ += number
        print(summ)
