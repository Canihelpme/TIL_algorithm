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