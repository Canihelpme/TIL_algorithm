"""
Deque or Queue사용
가장 위에 있는 문자 pop
두번째 문자는 pop한 다음 맨 밑에 append
길이가 1이 될때 까지 실행한 후 남은 값 print
Big(O) = n 시간 제한 확인해보길!
"""
#import Queue -> 잘 안씀 why? 느려. ->Thread 안전
from collections import deque #->Thread 비안전
n = int(input())
queue = []
for i in range(1, n+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    second = queue.popleft()
    queue.append(second)

print(queue.pop)
