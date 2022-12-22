# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


number = int(input("Введите число:"))
my_list = []
my_list = [round((1+1/number)**number, 2) for number in range(1, number+1)]
print(f'Последовательность:{my_list}') 
print(f'Сумма: {round(sum(my_list),2)}')