
target = [[6, 7, 12, 5], [5, 3, 11, 18], [7, 17, 3, 3], [8, 10, 14, 9]]
cache = [[-1 for i in range(5)]for j in range(5)]
cache2 = [0 for col in range(4)for row in range(4)]
direction = [[-1 for i in range(5)]for j in range(5)]
size = 5

def matrixPath(i, j):
    if cache[i][j] != -1:
        return cache[i][j]

    for i in range(0, 5):
        cache[i][0] = 0
        direction[i][0] = '-'

    for j in range(0, 5):
        cache[0][j] = 0
        direction[0][j] = '-'

    for i in range(1, 5):
        for j in range(1, 5):
            if i == 1 and j == 1:
                cache[i][j] = target[i - 1][j - 1]
                direction[i][j] = '-'
            elif i == 1:
               cache[i][j] = matrixPath(i, j - 1) + target[i - 1][j - 1]
               direction[i][j] = 1
            elif j == 1:
                cache[i][j] = matrixPath(i - 1, j) + target[i - 1][j - 1]
                direction[i][j] = 2
            else:
                minval = min(matrixPath(i - 1 , j), matrixPath(i, j - 1))
                cache[i][j] = minval + target[i - 1][j - 1]
                if minval == cache[i][j - 1]:
                    direction[i][j] = 1
                elif minval == cache[i - 1][j]:
                    direction[i][j] = 2
    return cache[i][j]

def printMatrixMinPath(i, j):
    if i == 0 and j == 0:
        print("경로(행, 열):")
    elif direction[i + 1][j + 1] == 1:
        printMatrixMinPath(i, j - 1)
    elif direction[i + 1][j + 1] == 2:
        printMatrixMinPath(i - 1, j)
    print(i, ',', j)
    
if __name__ == "__main__":

    i = len(target[0]) -1
    j = len(target) - 1
    print("행렬 최소 경로 값:", matrixPath(i, j))
    for k in cache:
        print(k)
    printMatrixMinPath(i, j)