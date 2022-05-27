import sys
array = list(map(int, [sys.stdin.readline().strip() for n in range(9)]))

#---정렬---
for i in range(1, len(array)):
    for j in range(i, 0 ,-1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break


#---합 구하기---
sum = 0
for i in range(9):
    sum += array[i]
    if sum == 100:
        print(array[0:i])
