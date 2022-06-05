n = int(input())
visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(dep):
    min_diff = 10000
        for i in range(n):
            for j in range(n):
                print("hi")
    
res = dfs(0,0)
print(res)                    