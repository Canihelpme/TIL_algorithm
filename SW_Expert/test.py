T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        a = 1
        print("#%d " % test_case + "%d" % 1)
    elif n == 2 and (arr[0] % 2) == (arr[1] % 2):
        print("#%d " % test_case + "%d" % -1)
    else:
        count = 0
        for i in range(1, n-1):
            if (arr[i] % 2) == (arr[i+1] % 2):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1
        print(arr)
        print("#%d " % test_case + "%d" % count)
