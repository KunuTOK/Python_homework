s = "Abracadabra"
print(s)
print('Вывести третий символ этой строки')
print(s[2])
print('Вывести предпоследний символ этой строки')
n = len(s)
print(s[n-2])
print('Вывести первые пять символов этой строки.')
print(s[:5])
print("Вывести строку, кроме последних двух символов")
print(s[:(n-2)])
print("Вывести все символы с четными индексами (считайте, что 0 - четный индекс)")
x=0
while  x <=n:
    if (x-1)%2:
        print(s[x], end='')
    x += 1
print()

print("Вывести все символы с нечетными индексами")
x=0
while  x <=(n-1):
    if x%2:
        print(s[x], end='')
    x += 1
print()
print("Вывести все символы в обратном порядке")
print(s[::-1])
print("Вывести все символы строки через один в обратном порядке, начиная с последнего.")
z=(s[::-1])
zx=0
while  zx <=n:
    if (zx-1)%2:
        print(z[zx], end='')
    zx += 1
print()
print("Вывести длину данной строки")
print(n)