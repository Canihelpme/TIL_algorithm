import sys
n, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

def selection_sort(array):
    count = 0

    for i in range(len(array) - 1, 0, -1):
        max_index = i
        for j in range(0, i+1):
            if array[max_index] < array[j]:
                max_index = j
        
        if array[i] != array[max_index]:
            array[i], array[max_index] = array[max_index], array[i]
            count += 1
        
        if count == k:
            return array[max_index], array[i]
              
    if count < k:
        return -1

print(selection_sort(array))
        
        
        
    