t = int(input())
res = 0
res += t // 1000
res += (t % 1000) // 100
res += (t%100) // 10
res += (t%10) // 1
print(res)