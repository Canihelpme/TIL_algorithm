#문자열 합치기
n = int(input())
for _ in range(n):
    a,b = input().split()
    a = int(a)
    str = list(b)
    result = ""
    for i in range(len(str)):
        result += "".join(str[i]*a)
    print(result)
    