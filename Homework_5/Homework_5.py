# Завдання 1:
text = input('Введіть слово:  ')
if text == text[::-1]:
    print("+")
else:
    print("-")

# Завдання 2:
text = input('Введіть текст:  ')
find = input('Яке слово будемо шукати? : ')
if find in text:
    print('Yes')
else:
    print('No')

# Завдання 3:
text = input('Введіть URL : ')
if text.startswith("abc"):
    text = "www" + text[3:]
else:
    text += "qqq"
print(text)

# Завдання 4:
s = input('Введіть текст:   ')
result = ' '
for i in s:
    if not i.isnumeric():
        result += i
print(result)

# Завдання 5:
mail = input('Enter your mail : ')
if '@' in mail and '.' in mail:
    print('+')
else:
    print('-')