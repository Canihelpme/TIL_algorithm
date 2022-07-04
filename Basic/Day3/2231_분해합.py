n = int(input())
res = []
for i in range(n+1):
    arr = list(str(i))
    sum = i
    for j in arr:
        sum += int(j)
    if sum == n:
        res.append(i)
if len(res) == 0:
    print(0)
final = min(res)
print(final)
"""
N = int(input())
result = 0

for i in range(1, N+1):        
    a = list(map(int, str(i)))  
    s = i + sum(a)              
    if(s == N):                 
        result = i                   
        break

print(result)
"""
