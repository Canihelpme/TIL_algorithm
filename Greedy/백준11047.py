number, amount = map(int, input().split())
coin_list = list()

print(number)
print(amount)

for i in range(number):
    coin_list.append(int(input()))
print(coin_list)

count = 0
for i in reversed(range(number)):
    count += amount//coin_list[i]
    amount = amount % coin_list[i]

print(reversed(range(number)))
print(count)