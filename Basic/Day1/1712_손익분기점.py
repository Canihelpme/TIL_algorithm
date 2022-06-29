import math
a,b,c = map(int, input().split())
n = 0

if b > c:
    print(-1)
elif b - c == 0:
    print(-1)
else:
    d = c - b
    e = int(a / d) + 1
    print(e)
