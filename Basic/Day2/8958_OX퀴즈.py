#List로 입력 받고
#0가 포인터 2개 사용해서 하나는 값 저장용도, 하나는 연속 판단 및 val 증가
n = int(input())
for _ in range(n):
    string = list(map(str, input()))
    sum = 0
    val = 1
    for i in string:
        if i == 'O':
            sum += val
            val += 1
        else:
            val = 1
    print(sum)
    