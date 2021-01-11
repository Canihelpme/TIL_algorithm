A = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def merge_sort(A, p = 0, r=None):
    if r is None: r = len(A)
    if p < r-1:
        q = int((p+r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)
    return (A)

def merge(A, p, q, r):
    B, i, j = [], p, q
    while True:
        if A[i] <= A[j]:
            B.append(A[i])
            i = i + 1
        else:
            B.append(A[j])
            j = j + 1
        if i == q:
            while j < r:
                B.append(A[j])
                j = j + 1
            break
        if j == r:
            while i < q:
                B.append(A[i])
                i = i + 1
            break
    A[p:r] = B