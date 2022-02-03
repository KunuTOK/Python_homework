def is_bigger(num1, num2, eps):
    # num1>=num2+eps
    x=(num1>=num2+eps)
    print(x)

num1, num2, eps= list(map(float, .split()))
