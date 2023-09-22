# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
from random import randint

min_limit = 0
max_limit = 1000
try_user = 10
count = 0

num1 = randint(min_limit, max_limit)  # обе границы входят в диапазон
while count < try_user:
    print("загаданное число : ", num1)
    count += 1
    print('Попытка ' + str(count))

    num_user = int(input('угадай число между ' + str(min_limit) + ' и ' + str(max_limit) + ': '))
    if num_user not in range(min_limit, max_limit + 1):
        print('число не входит в заданный диапазон, попытка потрачена  ')
    elif num_user > num1:
        print('твое число больше загаданного, попробуй еще ')
    elif num_user < num1:
        print('твое число меньше загаданного, попробуй еще ')
    elif num_user == num1:
        print('ты угадал! конец игры')
        break
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()
print('Было загадано число ', num1)

