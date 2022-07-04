from itertools import combinations

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
tri = []
for i in range(1, 45):
    tri.append(int((i*(i+1)) / 2))

for j in arr:
    res = 0
    for one in tri:
        for two in tri:
            for three in tri:
                if one + two + three == j:
                    res = 1
                    break
    print(res)
    