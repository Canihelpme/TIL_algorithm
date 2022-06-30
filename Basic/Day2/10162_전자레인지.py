n = int(input())
tmp = 0
res = []
while True:
    res.append(n // 300)
    tmp = n % 300
    res.append(tmp // 60)
    tmp = tmp % 60
    res.append(tmp // 10)
    tmp = tmp % 10
    if tmp == 0:
        for i in range(3):
            print(res[i], end=' ')
        break
    elif tmp != 0:
        print(-1)
        break
        