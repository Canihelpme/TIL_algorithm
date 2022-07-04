"""
1. "(",")" 둘이 만나면 펑하고 터져서 없어진다고 생각...
    -> 이걸 무수히 시행하면 괄호가 짝지어져 있으니 0이됨...
    열린 괄호가 나오면 따로 스택에 저장.
    이후 닫힌 괄호가 나오면 스택에 있는 가장 마지막의 열린 괄호 제거
    전체 괄호를 저장할 리스트와 열린 괄호를 저장할 스택 필요.
    결국 스택 or 리스트의 길이가 0이 아니면 vps가 아님.
"""
"""
1.괄호 쌍들로 이루어진 문자열 입력받음
2.여는 괄호:push
3.닫는 괄호:
    - 스택이 비어 있지 않으면 pop.
    - 스택이 비어잇으면 invalid 문자열.
4.위 과정을 반복해서 최정적으로 스택이 비어있으면 valid, else invalid.
Big(O)는 결국 N 그러나 TC 개수가 주어지면 TN이다.
"""

T = int(input())
for _ in range(T):
    S = input()
    stk = []
    isVPS = True
    for e in S:
        if e == '(':
            stk.append(e)
        else:
            if stk: #스택이 비어있지 않을 때
                stk.pop()
            else:
                isVPS = False
                break
    
    if stk:
        isVPS = False
    if isVPS:
        print("YES")
    else:
        print("No")