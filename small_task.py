# fibonacchi

a = 0
b = 1
i = 0

for _ in range(15):
    a, b = b, a + b
    print(a, end=' ')

while i < 15:
    a, b = b, a + b
    print(a, end=' ')
    i = i + 1
    
for _ in range(15):
    sum_ab = a + b
    a = b
    b = sum_ab
    print(a, end=' ')
    
# високосный год

year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')

# квадрат из символов с именем внутри

i = 0
name = input('Введите имя:')

while i < 11:
    if not i or i == 10:
            print('*' * 15)
    else:
        if i % 6 == 5:
            len_name = int((13 - len(name)) / 2)
            print('*{}{}{}*'.format(' ' * len_name, name, ' ' * len_name))
        else:
            print('*{}*'.format(' ' * 13))

    i = i + 1
    
# сумма всех чисел трехзначного числа


n = 999
# Извлекается первая цифра (старший разряд) числа
# путем делени нацело на 100
a = n // 100

# Деление нацело на 10 удаляет последнюю цифру числа.
# Затем нахождение остатка при делении на 10 извлекает
# последнюю цифру,которая в исходном числе была средней.
b = (n // 10) % 10

# Последняя цифра (младший разряд) числа находится
# путем нахождения остатка при делении нацело на 10.
c = n % 10

# Вычисляется сумма цифр и выводится на экран
print(a + b + c)

import string
import random
from pprint import pprint

letters_list = []

for _ in range(10000):
    letters_list.append(random.choice(string.ascii_letters))


letters_count_dict = {}

for letter in letters_list:
    if letter not in letters_count_dict:
        letters_count_dict[letter] = 1
    else:
        letters_count_dict[letter] = letters_count_dict[letter] + 1

pprint(letters_count_dict)
