import sys
n, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return(array[k-1])
print(insertion_sort(array))