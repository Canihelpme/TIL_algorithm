xList = []
yList = []
for _ in range(3):
    x,y = map(int, input().split())
    xList.append(x)
    yList.append(y)

for i in range(3):
    if xList.count(xList[i]) == 1:
        xResult = xList[i]
    if yList.count(yList[i]) == 1:
        yResult = yList[i]
print(xResult, yResult)