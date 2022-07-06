"""
1. n,m만큼 CD 갯수 받음.
2. 각자의 집합 생성 후 이 두 집합을 합침
3. 이때 전체 CD개수에서 집합의 크기를 빼면 겹치는 CD의 개수 알 수 있음
"""
import sys
input = sys.stdin.readline
while True:
    s = set()
    n,m = map(int, input().split())

    if n == m == 0:
        break

    for i in range(n):
        cd = int(input())
        s.add(cd)
        
    answer = 0
    for _ in range(n):
        cd = int(input())
        if cd in s:
            answer == 1
            print(answer)