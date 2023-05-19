n = int(input('Введіть число:  '))

if n % 2 != 0:
    if n > 20:
        print("Not Weird")
    else:
        print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")