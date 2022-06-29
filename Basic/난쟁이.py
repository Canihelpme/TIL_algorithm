#조합탐색, 브루트포스
#9C2 or 9C7  == O(1)
#브루트포스는 어케 해야하냐?
from itertools import combinations

arr = []
for _ in range(9):
    n = int(input())
    arr.append(n)

for e in combinations(arr, 7):
    result = sum(e)
    if result == 100:
        for i in e:
            print(i) 

elf_arr = [int(input()) for _ in range(9)] #맨위의 4줄과 같음 ㄷㄷ

#flag(조합 직접 구현시 사용가능) flag쓸 생각은 전혀 못했네