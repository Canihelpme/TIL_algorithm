import sys
sys.setrecursionlimit(10000) #최대 재귀 횟수설정
       
def dfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        n = x + dx[i]
        m = y + dy[i]
        
        if(0 <= n < N) and (0 <= m < M):
            if farm[n][m] == 1:
                farm[n][m] = -1
                dfs(n, m) #재귀호출 통해 자식(인접) node로
                
T = int(input()) # T 입력
for _ in range(T):
    M, N, K = map(int, input().split()) #M,N,K 입력 M-가로(X축) N-세로(Y축) 
    farm = [[0]*M for _ in range(N)] # 농장 생성
    #print(farm)
    count = 0 #에벌레 수
    
    for _ in range(K):
        a,b = map(int, input().split())
        farm[b][a] = 1
    #print(farm)
        
    for j in range(N):
        for k in range(M):
            if farm[j][k] == 1:
                dfs(j,k)
                count += 1
print(count)