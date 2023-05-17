# 1
a = {'Андрій', 'Сергій', 'Олександр', 'Марія', 'Оксана'}
b = {'Оксана', 'Андрій', 'Олексій', 'Сергій', 'Олександр', 'Іван'}

print('Імена боржників за Червень та Липень:')
print(a.intersection(b))

print('Імена боржників за Липень :')
print(b.difference(a))

# 2
camelcase_strings = ["FirstItem", "FriendsList", "MyTuple"]
snakecase_strings = []

for string in camelcase_strings:
    snakecase_string = ""
    for i, char in enumerate(string):
        if char.isupper():
            if i > 0:
                snakecase_string += "_"
            snakecase_string += char.lower()
        else:
            snakecase_string += char
    snakecase_strings.append(snakecase_string)

print(snakecase_strings)
