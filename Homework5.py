immutable_var = (1, 2, 'a', 'b')
print('Immutable_tuple:', immutable_var)
# При попытке внести изменения 'immutable_var[0] = 4' появляется ошибка, так как кортежи в Python не поддерживают изменения по элементам
mutable_list = [1, 2, 'a', 'b',]
mutable_list.append('Modified')
print('Mutable list:',mutable_list)