R, C = map(int, input().split())
map = []
dict = {}

for _ in range(R):
    map.append(list(input()))
count = 0

def dfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        n = x + dx[i]
        m = y + dy[i]
        if 0 <= n < R and 0 <= m < C and map[n][m] in dict == False:
            dict[str(map[n][m])] = 1
            dfs(n, m)
            count += 1
            
dict[str(map[0][0])] = 1
print(dict)
dfs(0,0)
print(count)