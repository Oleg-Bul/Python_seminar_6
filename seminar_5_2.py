# Задача 2.
# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'),
#  ..., ('ключ_N', 'значение_N'))
# Ввод:
# house=дом car=машина men=человек tree=дерево
# Вывод:
# (('house', 'дом'), ('car', 'машина'), ('men', 'человек'), ('tree', 'дерево'))


c = 'house=дом car=машина men=человек tree=дерево'
ListC = c.split(' ')
# ListC = list(c.items(' '.join(i for i in c.split(' '))))
a = {'house': 'дом', 'car': 'машина', 'men': 'человек', 'tree': 'дерево'}
b = list(a.items())
print(b)
print(ListC)
d = tuple(map(lambda x: tuple(x.split('=')), ListC))
# ListD = list(d.items(' '.join(i for i in d.split(' '))))
print(d)

a = 'house=дом car=машина men=человек tree=дерево'.split()
a = tuple(map(lambda x: tuple(x.split('=')), a))
print(a)
