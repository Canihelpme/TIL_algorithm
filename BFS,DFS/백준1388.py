import sys

n,m = map(int, input().split())
floor =  []
chk = [[False] * m for i in range(n)]
res = 0

for _ in range(n):
    floor.append(list(input()))

def is_valid(y,x):
    return 0 <= y < n and 0 <= x < m

def dfs(y,x):
    if not is_valid(y,x):
        return False

    if chk[y][x] ==  True:
        return False
    
    chk[y][x] = True
    if floor[y][x] == '-' and is_valid(y,x+1):
        if floor[y][x+1] == '-':
            dfs(y,x+1)
    elif floor[y][x]  == '|' and is_valid(y+1, x):
        if floor[y+1][x] ==  '|':
            dfs(y+1,x)
    return True

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            res += 1

print(res)