T = int(input())
for test_case in range(1, T+1):
    val = list(map(int, input().split()))
    res = round(sum(val) / 10)
    print(res)