T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    if a > b:
        print(">")
    elif a < b:
        print("<")
    elif a == b:
        print("=")