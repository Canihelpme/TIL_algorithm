n = input()
computers = input()
def solution(n, computers):
    i = 1
    adj = [[] * n for _ in range(n+1)]
    chk = [False] * n+1
    
    for row in adj:
        print(row)
        
    answer = 0
    return answer