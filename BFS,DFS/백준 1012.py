import sys

sys.setrecursionlimit(10 ** 6)
t = int(input())
   
for i in range(t):
    
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    
    cnt = 0
    width, length, q = map(int, input().split())
    farm = [[0] * width for _ in range(length)]
    chk = [[False] * width for _ in range(length)]
    
    for j in range(q):
        x,y = map(int, input().split())
        farm[y][x] = 1

    def valid_check(chk_y,chk_x):
        return 0 <= chk_y < length and 0 <= chk_x < width
    
    def dfs(start_y, start_x):
        if farm[start_y][start_x] == 0:
            return False
        
        if chk[start_y][start_x] == True:
            return False
        
        chk[start_y][start_x] = True
        for k in range(4):
            ny = start_y + dy[k]
            nx = start_x + dx[k]
            if(valid_check(ny, nx) and not chk[ny][nx] and farm[ny][nx] == 1): #결국 여기서 통과를 못하거나 False가 돼서 If문이 실행 안됨. 2번
                dfs(ny,nx) #결국 DFS를 통해서 마지막 노드에 가면...? 1번
        return True  #그럼 결국 True를 반환하게 됨 3번

    for a in range(length):
        for b in range(width):
            if dfs(a,b):
                cnt += 1
    print(cnt)
