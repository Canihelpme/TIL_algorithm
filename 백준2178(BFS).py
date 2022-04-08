"""import sys
import collections
input = sys.stdin.readline

n, m = map(int, input.split())
map = [list(map(int, input.split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

queue = deque()
queue.appned(0,0)
result = 0

while queue:
    y, x = queue.popleft()
    for i in range(n)
"""

import sys
import collections
input = sys.stdin.readline
    
n, m = map(int, input().split())    
map = [list(map(int, ' '.join(input()).split())) for _ in range(n)]

# 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = collections.deque([(0, 0)])
result = 0

while Q:
    print(Q)
    x, y = Q.popleft()
    print(Q)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if map[nx][ny] == 1:
                # 방문
                map[nx][ny] = map[x][y] + 1
                Q.append((nx, ny))

print(map)
print(map[n - 1][m - 1])
