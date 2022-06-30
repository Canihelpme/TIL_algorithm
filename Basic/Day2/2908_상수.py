#입력 값을 뒤집어서 처리
a,b = map(str, input().split())
a = "".join(reversed(a))
b = "".join(reversed(b))
print(max(a,b))