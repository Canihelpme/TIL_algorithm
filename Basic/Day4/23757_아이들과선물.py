#Big-O = (n+m)*logn
import sys
input = sys.stdin.readline

import heapq #빠름
n,m = map(int, input().split())
giftarr = list(map(int, input().split()))
wisharr = list(map(int, input().split()))

heap = []
for i in range(n):
    heapq.heappush(heap, -giftarr[i])
    
#heapq.heapify(heap) #heapify를 거치면 arr가 heap으로 변환됨

for i in range(m):
    wishCount = wisharr
    pop = heapq.heappop(heap)
    
    if pop < wishCount:
        print(0)
        exit(0)
    
    if pop == wishCount:
        continue

    remain = pop - wishCount
    heapq.heappush