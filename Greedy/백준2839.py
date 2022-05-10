
n = int(input())
"""
if  n == 4 or n == 7:
    print(-1)
elif n % 3 != 0 and n % 5 == 0:
    print(n // 5)
elif n % 3 == 0 and n % 5 != 0:
    print(n // 3)17
elif n % 3 == 0 and n % 5 ==0:
    print(n // 5)
"""

if n % 5 == 0:
    print(n // 5)
    
else:
    a = 0
    while n > 0:
        n -= 3
        a += 1
        if n % 5 == 0:
            a += (n // 5)
            print(a)
            break
        elif n == 1:
            print(-1)
            break
        elif n == 0: 
            print(a)
            break
            