a,b = map(int, input().split())
count = 0
for i in range(a+1):
    for j in range(60):
        for k in range(60):
            if (str(b) in str(i)) or (str(b) in str(j)) or (str(b) in str(k)):
                count += 1
            else:
                pass
print(count)