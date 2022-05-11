"""
for k in range(n*2):
    belt[k][0] = input_list[k]  #컨베이어 벨트와 로봇위치 확인할 리스트 생성
print(belt)

#벨트 이동
move = belt.pop(0)
belt.append(move)
print(belt)

#로봇 이동
move2 = belt[0][1]
print(move2)
for j in range(len(belt)-1):
    belt[j][1] =belt[j+1][1] 
belt[len(belt)-1][1] = move2
print(belt)

# robot이 위치해있으면 1 없으면 0


while True:
    #이동
    #move = belt.pop(0)
    #belt.append(move)
    #print(belt)
    
    #로봇 한칸씩 이동
    final_robot = belt[len(belt)-1][1]
    for j in range(len(belt)-1):
        if belt[j][0] != 0 and belt[j][1] != 1:
            robot_move = belt[j][1]
            belt[j+1][1] = belt[j][1]
    if belt[0][0] != 0 and belt[0][1] != 1:
        belt[0][1] = final_robot
        
    belt[0][1] = final_robot
    print(belt)

    for j
    count = 0
    for j in len(belt):
        if belt[j][0] == 0:
            count += 1
            if count > k-1:
                break
#print(conveyer(n,k,input,belt))
"""