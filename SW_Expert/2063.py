T = int(input())
res = list(map(int, input().split()))
res.sort()
print(res[T//2])