# task1
color = input('Твой любимый цвет: ')
if color == 'красный':
    print('Любитель яркого')
elif color == 'зелёный':
    print('Ты не охотник?')
elif color == 'синий':
    print('Ха, классика!')
else:
    print('Тебя не понять')

# task2

color = input('Твой любимый цвет: ')
match color:
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зелёный':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика!')
    case _:
        print('Тебя не понять')

# task3

year = int(input('Введите год в формате yyyy: '))
if year % 4 != 0:
    print("Обычный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")

# task 4

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введи число: '))
if num in data:
    print('Леонардо передаёт привет!')

# task 5

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введи число: '))
if num not in data:
    print('Леонардо грустит :-(')
# было :
my_math = int(input('2 + 2 = '))
if 2 + 2 == my_math:
    print('Верно!')
else:
    print('Вы уверены?')
# стало (тернарный оператор)

my_math = int(input('2 + 2 = '))
print('Верно!' if 2 + 2 == my_math else 'Вы уверены?')
# task 5

num = 42
name = 'Bob'
if num > 30:
    if num < 50:
        print('Вариант 1')
    elif name > 'Markus':
        print('Вариант 2')
    else:
        print('Вариант 3')
elif name < 'Markus':
    print('Вариант 4')
elif num != 42:
    print('Вариант 5')
else:
    print('Вариант 6')
# task 6
# Попробуем перебрать всё чётные числа от нуля до введённого пользователем исключительно..
num = float(input('Введите число: '))
count = 0
while count < num:
    print(count)
    count += 2

# Возврат в начало цикла, **************         continue        ********************
# Выведем все чётные числа (как в прошлом примере), кроме тех, которые кратны 12
num = float(input('Введите число: '))
STEP = 2
limit = num - STEP
count = -STEP
while count < limit:
    count += STEP
    if count % 12 == 0:
        continue
    print(count)

# Досрочное завершение цикла, ***************     break      ***************
# ввести число внутри заданного диапазона

min_limit = 0
max_limit = 10
while True:
    print('Введи число между', min_limit, 'и', max_limit, '? ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
print('Было введено число ' + str(num))

# Доработаем прошлую программу и дадим 3 попытки на попадание в диапазон.
min_limit = 0
max_limit = 10
count = 3
while count > 0:
    print('Попытка ' + str(count))
    count -= 1
    num = float(input('Введи число между ' + str(min_limit) + ' и    ' + str(max_limit) + ': '))
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()
print('Было введено число ' + str(num))

# Цикл итератор ***********************           for in      ****************
# Рассмотрим работу цикла в качестве итератора последовательности
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for item in data:
    print(item)

# Цикл по целым числам, он же
# арифметический цикл, функция range()

num = int(input('Введите число: '))
for i in range(0, num, 2):
    print(i)
# Цикл с нумерацией элементов, функция  *********        enumerate()       ***********
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)

#  задача1
data = 0
while data < 100:
    data += 2
    if data % 40 == 0:
        break
print(data)

#  задача2
data = 0
while data < 100:
    data += 3
    if data % 40 == 0:
        break
else:
    data += 5
print(data)

#  задача3
data = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    data += 1
    if data % 40 == 0:
        break
else:
    data += 5
print(data)
