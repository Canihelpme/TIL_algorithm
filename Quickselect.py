def partition(a, first, last):
    pivot = a[last]
    i = first - 1
    for j in range(first,last):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
            
    a[i+1], a[last] = a[last], a[i+1]
    return i+1

def select(a, first, last, tar):
    if first == last: return a[first]

    q = partition(a, first, last)

    k = q - first+1

    if tar < k:
        return select(a, first, q-1, tar)
    elif tar > k:
        return select(a, q+1, last, tar-k)
    else:
        return a[q]

a = [5, 7, 9, 0 , 3, 1, 6, 2, 4, 8]
tar = 3
first = 0
last = len(a) - 1
result = select(a, first, last, tar)
print(result)
