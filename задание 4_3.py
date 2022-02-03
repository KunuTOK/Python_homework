# задача 3
print("Введите три числа для сравнения")
var_1 = int(input('Введите A\n'))
var_2 = int(input('Введите B\n'))
var_3 = int(input('Введите C\n'))

if var_1 == var_2 == var_3:
# если True
   print("равны все 3 числа")
# иначе если выполняется другое условие
elif var_1 == var_2:
    print("равны все 2 числа")
elif var_1 == var_3:
    print("равны все 2 числа")
elif var_2 == var_3:
    print("равны все 2 числа")
else:
    print("числа не равны")      
