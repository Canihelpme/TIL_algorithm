#손님 숫자를 높이로 나눠 몫과 나머지를 통해 방 배정
#틀렸던 이유: 출력을 Str으로 출력해서
num = int(input())
for _ in range(num):
    h,w,n = map(int, input().split())
    #list = [[0 for col in range(w)] for row in range(h)]
    row = n // h + 1
    col = n % h
    if col == 0:
        row = n // h
        col = h
    print(col*100+row)   