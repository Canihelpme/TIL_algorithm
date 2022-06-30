#문자열에서 문자 갯수 찾기
a = int(input())
b = int(input())
c = int(input())
sum = a*b*c
for i in range(10):
    print(str(sum).count(f'{i}'))