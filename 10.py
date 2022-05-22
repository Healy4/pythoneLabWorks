'''
Реализовать функцию преобразования табличных данных. Входная и выходная таблицы заданы в построчной форме, с помощью списков. Заполненные ячейки имеют строковой тип данных. Пустые ячейки имеют значение None.

При преобразовании чисел сначала используется функция round() для округления до нужного числа знаков после запятой.

Над входной таблицей провести ряд преобразований:

Удалить дубли среди столбцов, оставив только первое вождение повторяющегося столбца в таблицу.
Удалить дубли среди строк, оставив только первое вождение повторяющейся строки в таблицу.
Удалить пустые строки.
Преобразовать содержимое ячеек по примерам.
'''

import re


def delete_empty_rows(table):
    return [row for row in table if row[0] is not None]


def d_d_c(table):
    for i in table:
        del i[2]
    return table


def d_d_r(table, num):
    state = 0
    for j in range(num, len(table)-1):
        state = table[j][3]
        num += 1
        for i in range(num, len(table)):
            try:
                if table[i][3] == state:
                    del table[i]
            except IndexError:
                return d_d_r(table, j)
    table = delete_empty_rows(table)
    return table


def transformer(table):
    pos = r"([a-z0-9_]*)\[at](\w*.\w*)"
    for j in table:
        str = j[1]
        mat = re.findall(pos, str)
        j[1] = mat[0][0]+'@'+mat[0][1]
        if int(j[0]):
            j[0] = 'Y'
        else:
            j[0] = 'N'
        j[3] = repr(round(float(j[3]), 1))
    return table


def transform(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = transformer(i, table[i][j])
    return table


def transformName(table):
    name = r"""^([А-Яа-я])*"""
    for i in table:
        str = i[2]
        matches1 = re.search(name, str)
        i[2] = matches1[0]
    return table


def main(table):
    return transformer(
        transformName(
            d_d_r(
                delete_empty_rows(
                    d_d_c(table)
                ), 0
            )
        )
    )

table1 = [['0', 'retev57[at]rambler.ru', 'Ретев Семен', 'Ретев Семен', '0.902'], 
['1', 'ribozan89[at]yahoo.com', 'Рибоцян Гордей', 'Рибоцян Гордей', '0.173'], 
['1', 'valerij56[at]yahoo.com', 'Догман Валерий', 'Догман Валерий', '0.984'], 
[None, None, None, None, None], 
['0', 'robert18[at]yahoo.com', 'Тучий Роберт', 'Тучий Роберт', '0.038'], 
[None, None, None, None, None], 
['0', 'robert18[at]yahoo.com', 'Тучий Роберт', 'Тучий Роберт', '0.038'], 
['0', 'robert18[at]yahoo.com', 'Тучий Роберт', 'Тучий Роберт', '0.038']]
    
    
table = [
    [None, None, None, None, None], 
    ['1', 'daniel_44[at]mail.ru', 'Шефов Даниэль', 'Шефов Даниэль', '0.104'], 
    ['0', 'zuzskij72[at]gmail.com', 'Цузский Дмитрий', 'Цузский Дмитрий', '0.332'], 
    [None, None, None, None, None], 
    ['0', 'munazic84[at]rambler.ru', 'Муназич Петр', 'Муназич Петр', '0.374'], 
    ['0', 'zuzskij72[at]gmail.com', 'Цузский Дмитрий', 'Цузский Дмитрий', '0.332'], 
    ['0', 'zuzskij72[at]gmail.com', 'Цузский Дмитрий', 'Цузский Дмитрий', '0.332']
]
print(main(table1))
