#List로 단어 입력 받음
#아스키코드 사용하여 알파벳 비교
string = input()
check = [-1]*26
for i in range(len(string)):
    if check[ord(string[i])-97] != -1:
        continue
    else:
        check[ord(string[i])-97] = i
        
for i in range(26):
    print(check[i], end=' ')