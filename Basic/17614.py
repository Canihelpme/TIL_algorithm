#369문제
n = int(input())

count = 0
for i in range(1, n+1):
    strI = str(i)
    for j in strI:
        if j == '3' or j == '6' or j =='9':
            count += 1
        
##시간복잡도는 nLogN ##

for k in range(1, n+1):
    while k != 0:
        fir_d = k % 10
        if fir_d % 3 ==0 and fir_d != 0: #앞에 조건만 있으면 1의자리가 0일때 문제 발생
            count += 1
        k //= 10
        
        
