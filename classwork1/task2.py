n = int(input('Введите число n: '))
e = int(input('Введите число e: '))
count1 = 0  # количество чисел
sum1 = 0  # сумма чисел
i = 0
# while i < n:
#     i += 1
#     if i % e == 0:
#         continue
#     elif i % 2 == 0:
#         count1 += 1
#         sum1 += i
# print(count1)
# print(sum1)
# *********************** 2 вариант ******************
while i < n:
    i += 1
    if i % 2 == 0 and i % e != 0:
        sum1 += i
        count1 += 1
print(sum1)
print(count1)



