immutable_var = 2, 35, 'браслет', '3'
print(immutable_var)
immutable_var[0] = 5
# не получается изменить т.к. символ является неизменяемым объектом внутри кортежа

mytable_list = 'Headphones', ['mouse', 56], 98
print(mytable_list)
mytable_list[1][0] = 32
print(mytable_list)