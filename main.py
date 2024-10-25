'''
На вход программе подаются номера телефонов, записанные в одну строчку через пробел, 
с разными кодами стран: +7, +6, +2, +4 и т.д. Необходимо прочитать строку и на ее основе сформировать словарь d. 
Ключами словаря должны быть коды (строки: +7, +6, +2 и т. п.), а значениями список номеров в виде строк 
(следующих в том же порядке, что и в исходной строке) с соответствующими кодами. 
'''

numbers = [[x[:2], x] for x in input().split()]

d = {}

for i in numbers:
    if i[0] not in d:
        d[i[0]] = []
        d[i[0]].append(i[1])
    else:
        d[i[0]].append(i[1])

print(*sorted(d.items()))

