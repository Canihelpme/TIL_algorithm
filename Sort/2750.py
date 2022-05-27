import sys
n = int(sys.stdin.readline())
array = [sys.stdin.readline().strip() for i in range(n)]
array = list(map(int, array))

def selection(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return(array)

for k in selection(array):
    print(k)