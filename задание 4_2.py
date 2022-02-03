# задача 2
print("Введите три числа и узнаете какое меньш-")
var_1 = int(input('Введите A\n'))
var_2 = int(input('Введите B\n'))
var_3 = int(input('Введите C\n'))

if var_1 == var_2 == var_3:
# если True
   print("Числа равны")
# иначе если выполняется другое условие
elif var_1 < var_2:
# если True для elif
    if var_1 < var_3:
        print(var_1)
    else:
        print(var_3)
elif var_2 < var_1:
    # если True для elif
    if var_2 < var_3:
        print(var_2)
    else:
        print(var_3)      

1