import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
input_list = list(map(int, input().split()))
belt = [[0]*(2*n)]

for j in range (n*2):
    belt[j][0] = input_list[j] #conveyer belt 입력
print(belt)

for k in range(len(input_list)):
    input_list[k][1] = 0
print(input_list)

"""
belt = [[0]*(n*2)]
result = 1

for k in range(n*2):
    belt[k][0] = input_list[k]  #컨베이어 벨트와 로봇위치 확인할 리스트 생성
print(belt)

#벨트 이동
move = belt.pop(0)
belt.append(move)
print(belt)

#로봇 이동
move2 = belt[0][1]
print(move2)
for j in range(len(belt)-1):
    belt[j][1] =belt[j+1][1] 
belt[len(belt)-1][1] = move2
print(belt)
"""