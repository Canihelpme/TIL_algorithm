def linearSelect(a, first, last, tar):
    i = 0
    if first == last: return a[first]
    
    elif(len(a) <= 5):
        for i in range(len(a)):
            if i == tar: return a[i]
    
    q = linear_partition(a, first, last)
    
    if q > tar: return linearSelect(a, first, q - 1, tar)
    elif q == tar: return a[q]
    else: return linearSelect(a, q+1, last, tar)

def linear_partition(a, first, last):

    pivot_index = findPivot(last)
    a[pivot_index], a[last] = a[last], a[pivot_index]

    pivot = a[last]
    i = first - 1
    j = first
    return pivot

def findPivot(last):
    arr = []
    index = 0
    pivot = 2

    if last % 5 == 0:
        arr = [last/5]
    else:
        arr = [last/5+1]
    
    while(pivot <= last):
        arr[index] = pivot
        pivot += 5
        index += index
    mid = len(arr)/2
    c = int(mid)
    return arr[c]

a = [5, 7, 9, 0 , 3, 1, 6, 2, 4, 8]
tar = 3
first = 0
last = len(a) - 1
result2 = linearSelect(a, first, last, tar)
print(result2)