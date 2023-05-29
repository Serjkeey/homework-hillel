# 1
# import pickle
# # Створюємо словник з данними
# contact = [
#     {'Alex': '+380997654513'},
#     {'Andrew': '+380675690061'},
#     {'Serhii': '+380661238812'}
# ]
# file_name = 'contact.bin'
# with open('contact.bin', 'wb') as file:
#     pickle.dump(contact, file)
# перевірка
# test= open('contact.bin', 'rb')
# contact = pickle.load(test)
# print(contact)


# 2
import json
import json

a = {'key': 1, 'key2': True}
b = {'key': 'Hello'}
c = {}
for key, value in a.items():
    if key in b:
        c[key] = [value, b[key]]
    else:
        c[key] = value

for key, value in b.items():
    if key not in c:
        c[key] = value

with open('result.json', 'w') as file:
    json.dump(c, file)
