user_password = input('Введіть ваш пароль, для перевірки надійності:  ')

score = 0

# Перевіряємо довжину пароля.
if len(user_password) < 8:
    print('Пароль має бути більше, або дорівнювати 8 символам')
else:
    score += 1

# Перевіряємо, чи є в паролі велика літера
has_upper = False
for u in user_password:
    if u.isupper():
        has_upper = True
if not has_upper:
    print('Пароль має містити хоча б одну велику літеру')
if has_upper:
    score += 1

# Перевіряємо, чи є в паролі маленька літера
has_lower = False
for l in user_password:
    if l.islower():
        has_lower = True
if not has_lower:
    print('Пароль має містити хоча б одну маленьку літеру ')
if has_lower:
    score += 1

# Перевіряємо, чи є в паролі цифра
has_number = False
for n in user_password:
    if n.isdigit():
        has_number = True
if not has_number:
    print('Пароль має містити хочаб одну цифру')
if has_number:
    score += 1

# перевіряємо, чи є в паролі спеціальний символ
has_symbol = False
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '<', '>', '?']
for s in user_password:
    if s in symbol:
        has_symbol = True
if not has_symbol:
    print('Пароль має містити хоча б один спеціальний символ')
if has_symbol:
    score += 1

print('Рахунок вашого паролю: ', score)
