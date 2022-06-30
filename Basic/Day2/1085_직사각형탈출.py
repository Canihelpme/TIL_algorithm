x,y,w,h = map(int, input().split())
xResult = w-x
yResult = h-y
print(min(x, y, xResult, yResult))