# задача 5
n = int(input("Введите число от 1 до 9: ")) + 1
for i in range(1, n + n + 2):
    if i <= n:
        print(' ' * (n - i), end='')
        print(*range(1, i), *range(1, i - 1)[::-1], sep='')
    else:
        print(' ' * (i - n), end='')
        print(*range(1, n + n - i), *range(1, n + n - i - 1)[::-1], sep='')