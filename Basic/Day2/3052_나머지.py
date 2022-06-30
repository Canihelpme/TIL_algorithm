#List 생성해서 나머지 모두 저장하고 count로 갯수 확인하여 list 저장
#list[i] 값 0인것 제외
tmp_list = []
for i in range(10):
    a = int(input())
    tmp_list.append(a%42)
tmp_list2 = []
for i in range(43):
    tmp_list2.append(tmp_list.count(i))
print(43-(tmp_list2.count(0)))