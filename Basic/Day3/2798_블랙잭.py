from itertools import combinations
a,b = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for e in combinations(arr, 3):
    if result < sum(e) and sum(e) <= b:
        result = sum(e)
print(result)