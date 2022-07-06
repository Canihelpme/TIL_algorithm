from collections import deque
n = int(input())

dq = deque()
for i in range:
    card = n - i
    dq.appendleft(card)
    
    for _ in range(card):
        lastCard = dq.pop()
        dq.appendleft(lastCard)

print(*dq) 
#*를 붙이면 원소만 깔끔하게 보여줌.
# == while dq: print(dq.popleft(), end=' ')