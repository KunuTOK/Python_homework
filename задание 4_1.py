# задача 1
print("Введите два числа и узнаете какое меньш-")
var_1 = int(input('Введите A\n'))
var_2 = int(input('Введите B\n'))

if var_1 == var_2:
# если True
   print("Числа равны")
# иначе если выполняется другое условие
elif var_1 < var_2:
# если True для elif
    print(var_1)
# если False для всех
else:
    print(var_2)
1