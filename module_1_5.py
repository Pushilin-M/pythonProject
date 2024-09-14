immutable_var = 12,13.3,'элемент',True,
print(immutable_var)

#immutable_var [1] = 13
#print(immutable_var)
#'tuple' object does not support item assignment
# Объект «кортеж» не поддерживает назначение элементов

mutable_list = [1, 9.3,'элемент', True]
mutable_list [1] = 8
mutable_list [2] = 'element'
print(mutable_list)