n = int(input())
arr = list(map(int, input().split()))
if n == 2:
    for i in range(1, min(arr)+1):
        if arr[0]%i == 0 and arr[1]%i == 0:
            print(i)
elif n == 3:
    for i in range(1, min(arr)+1):
        if arr[0]%i == 0 and arr[1]%i == 0 and arr[2]%i==0:
            print(i)        
    