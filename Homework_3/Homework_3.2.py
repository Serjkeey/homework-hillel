n = int(input('Введіть ширину трикутника:\n'))

# Трикутник 1:
for i in range(n, 0, -1):
    print('*' * i)

# Трикутник 2:
for i in range(1, n + 1):
    print('*' * i)

# Трикутник 3:
for i in range(n):
    print(' ' * i + '*' * (n-i))

# Трикутник 4:
for i in range(n):
    print(' ' * (n-i-1) + '*' * (i+1))
