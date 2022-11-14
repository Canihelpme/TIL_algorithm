dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

chk = [[False] * 100 for _ in range(100)]
N = int(input())

def is_valid_coord(y, x):
    return 0<= y < N and 0<= x < N

def  dfs(start_y, start_x):
    chk[start_y][start_x] = True
    for k in range(4):
        ny = start_y + dy[k]
        nx = start_x + dx[k]
        if(is_valid_coord(ny, nx) and not chk[ny][nx]):
            dfs(ny, nx)

