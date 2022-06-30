n = int(input())
sum = 0
valList = list(map(int, input()))
for i in range(len(valList)):
    sum += valList[i]
print(sum)