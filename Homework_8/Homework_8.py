n = int(input("Яку кількість файлів бажаєте додати? :"))
files = {}
for i in range(n):
    file_line = input().split()
    files[file_line[0]] = file_line[1:]
m = int(input("Скільки буде запитів до файлів? :"))
for i in range(m):
    operation_line = input().split()

    operation_to_check = operation_line[0]
    file = operation_line[1]

    permitted_operations = files[file]

    if operation_to_check == "read":
        operation_to_check = 'R'
    elif operation_to_check == "write":
        operation_to_check = 'W'
    elif operation_to_check == "execute":
        operation_to_check = 'X'
    else:
        print("Unknown operation")
        continue

    if operation_to_check in permitted_operations:
        print("OK")
    else:
        print("Access denied")