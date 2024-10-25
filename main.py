'''
 На вход программе поступают номера телефонов с привязкой к именам в виде строк следующего формата:
номер_1 имя_1
номер_2 имя_2
...
номер_N имя_N
В программе уже реализовано считывание всех строк и сохранение их в виде списка:
lst_in = list(map(str.strip, sys.stdin.readlines()))
На основе списка lst_in необходимо создать словарь d, где ключами будут имена, 
а значениями - список номеров телефонов для этого имени (ключа). Обратите внимание, что одному имени может
 принадлежать несколько разных номеров.
'''
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
lst = [[x.split()[1], x.split()[0]] for x in lst_in]

d = {}

for i in lst:
    if i[0] not in d:
        d[i[0]] = []
        d[i[0]].append(i[1])
    else:
        d[i[0]].append(i[1])

print(*sorted(d.items()))


