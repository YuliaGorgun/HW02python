# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random
my_list = []
new_list = []
for i in range(10):
    my_list.append(i)
print(my_list)
while my_list:
    current_list = my_list.pop()
    new_list.append(current_list)
list_length = len(new_list)
for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = new_list[i]
        new_list[i] = new_list[index_aleatory]
        new_list[index_aleatory] = temp
print(new_list)



