# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
n= int(input("Введите число монет: "))
count = 0
list_1 = [randint(0,1) for i in range(n)]
#print(*list_1)
for j in list_1:
    if j == 0:
        count+=1
print("Нужно перевернуть", count)