"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

"""Вывод:
Мне кажется что первый вариант более эфективен поскольку у него сложность меньше, 
что дает на разных машинах более быстрое вычисление"""

"""Сложность: O(NlogN) """
# Первый вариант
list_company = [{'Company': 'Microsoft', 'Profit': 39240}, {'Company': 'Intel', 'Profit': 21048},
                {'Company': 'Cisco Systems', 'Profit': 11621}, {'Company': 'Amazon', 'Profit': 11588},
                {'Company': 'Apple', 'Profit': 55256},
                {'Company': 'Facebook', 'Profit': 18485}]                              # O(1)
newlist = sorted(list_company, key=lambda k: k['Profit'], reverse=True)                # O(NlogN)
print(f'1 место {newlist[0]} \n2 место {newlist[1]} \n3 место {newlist[2]}')           # O(1)

# Второй вариант
"""Сложность: O(N^2) """
list_company_2 = [{'Microsoft': 39240}, {'Intel': 21048},
                  {'Cisco Systems': 11621}, {'Amazon': 11588},
                  {'Apple': 55256},
                  {'Facebook': 18485}]                                     # O(1)
sort_ed = True                                                             # O(1)
while sort_ed:
    sort_ed = False                                                        # O(1)
    for el in range(len(list_company_2) - 1):                              # O(N)
        for key, value in list_company_2[el].items():                      # O(N)
            for key_2, value_2 in list_company_2[el + 1].items():          # O(1)
                if value < value_2:                                        # O(1)
                    list_company_2[el], list_company_2[el + 1] = list_company_2[el + 1], list_company_2[el]  # O(1)
                    sort_ed = True                                                                           # O(1)
print(f'1 место {list_company_2[0]}\n2 место {list_company_2[1]}\n3 место {list_company_2[2]}')              # O(1)
