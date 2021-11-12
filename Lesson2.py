# Заменить все буквы "x" на "y"
print("Задание 1")
line = "box fox fix mix taxi oxygen excuse explain six taxes excellent"
new_line = ""
for ch in line:
    if ch == "x":
        new_line += "y"
    else:
        new_line += ch
print(line)
print(new_line)

# Сосчитать поизведение чисел, кратных 3 и 5
print("Задание 2")
числа = [1, 9, 3, 45, 5, 6, 5, 4, 55, 4, 155]
произведение = 1
for x in числа:
    if x % 5 == 0 and x % 3 == 0:
        произведение *= x
print(произведение)

# Заменить все буквы "x" на "y" в исходной строке
# без использования дополнительной
print("Задание 3")
print(line)
line = line.replace("x", "y")
print(line)

vars = [1, 1.1, "abc", 'def', [1, 2], (1, 2), {1: 2}, None]
for x in vars:
    print(x, type(x))

# Опишите образ, используя список
kim_sungkyu_list = ['김성규', 28, 4, 1989, 'Infinite']
print(kim_sungkyu_list)

# Опишите образ, используя словарь
kim_sungkyu_dict = {'Name': '김성규', 'Date of birth': 28, 'Month of birth': 4,
                    'Year of birth': 1989, 'Group': 'Infinite'}
print(kim_sungkyu_dict)
