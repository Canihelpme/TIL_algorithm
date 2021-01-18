import sys
import math
input = sys.stdin.readline
n = int(input())
m = [[0] * n for i in range(n)]
d = [list(map(int, input().split())) for i in range(n)]

for r in range(1, n):
    m[r][r] = 0
    for i in range(n - r):
        j = i + r
        m[i][j] = math.inf
        for k in range(i, j):
            m[i][j] = min(m[i][j], m[i][k] + m[k + 1][j] + d[i][0] * d[k][1] * d[j][1])
print(m[0][n - 1])