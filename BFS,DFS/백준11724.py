import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n,m  = map(int, input().split())
adj = [[0] * n for _ in range(n)]

for _ in range (m):
    x,y = map(int, input().split())
    y -= 1
    x -= 1
    adj[y][x] = adj[x][y] =  1

res = 0
chk = [False] * n

def dfs(now):
    for nxt in range(n):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)
   
for i in range(n):
    if not chk[i]:
        res += 1
        chk[i] = True
        dfs(i)

print(res)
        
        
