#https://www.acmicpc.net/problem/1316
#연속된 군집 개수 출력
n = int(input())
count = n

for i in range(n):
    str = input()
    for j in range(len(str)-1):
        if str[j] == str[j+1]:
            pass
        elif str[j] in str[j+1:]:
            count -= 1
            break
print(count)