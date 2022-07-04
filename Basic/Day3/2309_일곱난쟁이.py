"""
from itertools import combinations
tmp1, tmp2 = 0, 0
arr = []
for _ in range(9):
    n = int(input())
    arr.append(n)

for i in range(9):
    for j in range(i+1, 9):
        if sum(arr) - (arr[i]+arr[j]) == 100:
            tmp1 = arr[i]
            tmp2 = arr[j]

arr.remove(tmp1)
arr.remove(tmp2)

print('\n'.join(map(str, sorted(arr))))"""
from itertools import combinations

arr = []
for _ in range(9):
    n = int(input())
    arr.append(n)

for e in combinations(arr, 7):
    result = sum(e)
    if result == 100:
        e = list(e)
        e = sorted(e)
        for i in e:
            print(i)