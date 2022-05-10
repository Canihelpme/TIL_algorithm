n = int(input())
schedule = []

for _ in range(n):
  schedule.append(list(map(int, input().split())))

schedule.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = schedule[0][1]

for i in range(1, n):
  if end_time <= schedule[i][0]:
    end_time = schedule[i][1]
    count += 1

print(count)
