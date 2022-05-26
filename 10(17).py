import re


def d_d_c(table):
    for i in table:
        del i[0]
        del i[1]
    return table


def toFixed(numObj, digits=0):
    return f'{numObj:.{digits}f}'


def transformer(table):
    pos = r"(\d.\d*)#(\d*)\/(\d*)\/(\d*)"
    for j in table:
        str = j[1]
        mat = re.findall(pos, str)
        for i in mat:
            j[1] = i[3]+'.'+i[2]+'.'+i[1]
            j.append(toFixed(float(i[0]), 4))
        if j[2] == 'Y':
            j[2] = '1'
        else:
            j[2] = '0'
    return table


def transform(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = transformer(i, table[i][j])
    return table


def transformName(table):
    name = r"([А-Яа-я]*)\s\S.\s([А-Яа-я]*)"
    for i in table:
        str = i[0]
        matches = re.findall(name, str)
        for j in matches:
            i[0] = j[1]+' '+j[0]
    return table


def main(table):
    return transformer(
        transformName(
                d_d_c(table)
        )
    )
    
table1 = [
[None,'Владислав У. Чосушский',None,'0.393#01/05/26','N'],
[None,'Святогор Т. Сезафко',None,'0.903#99/12/07','Y'],
[None,'Юрий Л. Сецунли',None,'0.125#04/10/07','Y'],
[None,'Мирослав Ф. Бомян',None,'0.358#00/09/04','Y']
]
print(main(table1))
