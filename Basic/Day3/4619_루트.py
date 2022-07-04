while True:
    b, n = map(int, input().split())
    if b == n == 0:
        break
    i = 0
    for i in range(1, 1000001):
        num1 = abs(i**n - b)
        num2 = abs((i+1)**n - b)
        res = 1000000
        if res > num1:
            res = num1
        if res > num2:
            res = num2
    print(res)