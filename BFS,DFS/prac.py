from collections import deque

def soultion(n, edge):
    adj = [[] *n for _ in range(n+1)]
    visit = [0] * (n+1)
    
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)

    visit[1] = 1
    q = deque([1])
    while q:
        x = q.popleft()
        for nxt in adj[x]:
            if not visit[nxt]:
                visit[nxt] = visit[x]+1
                q.append(nxt)
    max_v = max(visit)
    result = visit.count(max_v)
    return result