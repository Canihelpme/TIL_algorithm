a,b,c,d = map(int, input().split())
n = 1000
aResult = []
bResult = []
res = []
for i in range(1001):
    aResult.append(a*i+c)
    bResult.append(b*i+d)
for i in aResult:
    for b in bResult:
        if i == b:
            res.append(i)
if len(res) == 0:
    print(-1)
elif len(res) > 0:
    print(res[0])                
    