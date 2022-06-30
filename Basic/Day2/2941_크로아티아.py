#https://www.acmicpc.net/problem/2941
#크로아티아 문자 개수 카운팅 후 크로아티아 문자 제거
#카운팅 결과와 남은문자 개수 더하여 결과 
str = str(input())
cz = ['c=', 'c-', 'dz=', 'd-','lj','nj','s=','z=']
count = 0
for i in range(len(cz)):
    res = str.count(cz[i])
    str = str.replace(cz[i], ",")
    if res > 0:
        count += res
str = str.replace(",", "")
print(count+len(str))
