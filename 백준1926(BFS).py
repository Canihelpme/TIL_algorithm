"""
1. 아이디어
- 2중 for => 값 1 && 방문하지 않은 곳만 => BFS
- BFS 돌면서 그림 개수 +1 , 그림 개수 갱신

2. 시간복잡도
- BFS: O(V+E)
- V: 500 * 500
- E: 500 * 500 * 4
- V+E : 5 * 250000 = 100만 

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문여부 : bool[][]
- Queue(BFS)
"""d
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)] #map setting
chk = [[False] * m for _ in range(n)] #방문여부 mapping

#오른쪽, 아래, 왼쪽, 위 방향으로 이동
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#j = y, i = x
def bfs(y, x):
    res = 1
    queue = deque()
    queue.append((y,x))
    print(queue,"start")
    while queue:
        ey, ex = queue.popleft()
        print("pop left",ey,ex,"&& Search from",ey,ex)
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    res += 1
                    chk[ny][nx] = True
                    queue.append((ny,nx))
                    print(queue)
    print("--------")
    return res
            
cnt = 0
maxSize = 0

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            #방문 변경
            chk[j][i] = True
            #전체 그림 갯수 + 1
            cnt += 1
            # BFS
            #최대 사이즈 갱신
            maxSize = max(maxSize, bfs(j,i))

print(cnt)
print(maxSize)