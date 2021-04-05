"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
В ф-цию принимаются два элемент - это левая и правая части

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def task_7(x, y):
    if x == 0:
        return f'Полученое число рекурсией {y}'
    return task_7(x - 1, y + x)


x = int(input('Введите число'))
print(task_7(x=x, y=0))
print(f'Полученое число в уравнение {(x * (x + 1) / 2)}')
