"""
-----vector-----
v = []
v.append((123, 456))
v.append((789, 987))
print("size", len(v))
for p in v:
    print(p)
"""

#queue
"""
from collections import deque
q = deque()
q.append(123)
q.append(456)
q.append(789)
print("size", len(q))
print(q)
while len(q) > 0:
    print(q.popleft())
    print(q)
"""

#Priority Queue
"""
import heapq
pq = []
heapq.heappush(pq, 456)
heapq.heappush(pq, 123)
heapq.heappush(pq, 789)
print("size:", len(pq))
while len(pq) > 0:
    print(heapq.heappop(pq))
"""
"""
#DFS
import sys

sys.setrecursionlimit(10 ** 6)
adj = [[0] * 13 for _ in range (13)]

adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1

for row in adj:
    print(row)

def dfs(now):
    for nxt in range (13):
        dfs(nxt)

dfs(0)
"""
#이걸 보니 쉽게 이해가 되네

#BFS
"""
from collections import deque

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1

def bfs():
    dq = deque()
    dq.append(0)
    while dq: #큐가 비워질때 까지 반복
        now = dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)

bfs()
"""
from heapq import heappush, heappop, heapify

answer = []
heappush(answer, 10)
print(answer)
heappush(answer, -11)
print(answer)
heappush(answer, -18)
heappush(answer, -5)
heappush(answer, 8)
heappush(answer, 98)
print(answer)
heapify(answer)
print(answer)        
            
            
        
        
        
    
