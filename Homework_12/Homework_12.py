# 1 :
def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst


my_list = [1, 2, 3, 4, 5]
print(change(my_list))

# 2 :
def to_dict(lst):
    dictionary = {}
    for element in lst:
        dictionary[element] = element
    return dictionary


my_list = ['John', 'Bob', 'Andrew', 'Max']
print(to_dict(my_list))

# 3 :
def sum_range():
    start = int(input("Введіть початкове число: "))
    end = int(input("Введіть кінцеве число: "))

    if start > end:
        start, end = end, start

    total = 0
    for num in range(start, end + 1):
        total += num
    return total


result = sum_range()
print(f'Сумма чисел = {result} ')
