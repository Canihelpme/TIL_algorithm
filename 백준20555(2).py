from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
input_deque = deque(map(int, input().split()))
print(input_deque)
robot_deque = deque([0]*(n))
print(robot_deque)
result = 1

while True:
    #move
    input_deque.rotate(1) #belt 한칸 씩 이동(오른쪽으로)
    robot_deque.rotate(1) #robot 한칸 씩 이동(오른쪽으로)
    robot_deque[n-1] = 0 #컨베이어 벨트의 윗부분 로봇 하차
    
    #robot move
    for i in range(n-1, -1, -1): #(start, end, step)
        if(robot_deque[i] != 0 and robot_deque[i+1]==0 and input_deque[i+1] >= 1):
            input_deque[i+1] -= 1
            robot_deque[i+1] = robot_deque[i]
            robot_deque[i] = 0
    robot_deque[n-1] = 0
    
    #Placing robot
    if robot_deque[0] == 0 and input_deque[0] > 0:
        input_deque[0] -= 1
        robot_deque[0] = 1
    
    #Check abil
    cnt = 0
    for i in range(len(input_deque)):
        if input_deque[i] == 0:
            cnt += 1
    if cnt >=k:
        print(result)
        break

    result += 1
    
    #시간복잡도 n
    #구현하는데 3시간
    #생각하는데 30분