from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(x, y):
    rs = 1
    q = deque()
    q.append((x, y))
    print(q,"start")
    while q:
        ex, ey = q.popleft()
        print("pop left",ex,ey,"&& Search from",ex,ey)
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if map[nx][ny] == 1 and chk[nx][ny] == False:
                    rs += 1
                    chk[nx][ny] = True
                    q.append((nx,ny))
                    print(q)
    print("--------")
    return rs

cnt = 0
maxv = 0
print(n,m)

for i in range(m):
    for j in range(n-1):
        if map[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            cnt += 1
            maxv = max(maxv, bfs(i,j))

print(cnt)
print(maxv)

# 생각하기 편한대로 x,y를 변경했을 시 
# input마저도 변경이 되어 그림 자체가 x,y가 변환되어 나타남
