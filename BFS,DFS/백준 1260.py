from collections import deque

n,m,v = map(int, input().split())
adj = [[0] * n for _ in range(n)]

for _ in range(m):
    v1,v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    adj[v1][v2] = adj[v2][v1] = 1
    
chk = [False] * n

def valid_check(y, x):
    return 0 <= y < n and 0 <= x < n

def dfs(now):
    chk[now] = True
    print(now+1, end=" ")
    for nxt in range (n):
        if adj[now][nxt] == 1 and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

dfs(v-1)
#-----DFS-----#

chk2 = [False] * n

def bfs(now):
    now = now-1
    q = deque()
    q.append(now)
    chk2[now] = True
    while q:
        now = q.popleft()
        print(now+1, end=" ")
        for i in range(0, n):
           if chk2[i] == False and adj[now][i] == 1:
               q.append(i)
               chk2[i] = 1
print()
bfs(v)
    
    



    