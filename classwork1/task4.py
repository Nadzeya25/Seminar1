# Задание №8
# нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# number = int(input("Сколько рядов у елки? - "))
# branch = 1
# for elem in range(number):
#     print(' '*(number - elem), branch*"*")
#     branch += 2

number = int(input("Сколько рядов у елки? - "))
for i in range(1, number + 1):
    print(" " * (number - i) + "*" * (2 * i - 1))



