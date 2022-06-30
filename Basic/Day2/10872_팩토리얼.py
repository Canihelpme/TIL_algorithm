#재귀함수 혹은 변수 1개에 계속 곱하기
#0부터 시작하지 않도록 for문 범위 조정
n = int(input())
result = 1
for i in range(1, n+1):
    result = result * i
print(result)