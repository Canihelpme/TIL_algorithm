t = int(input())
for tc in range(1, t+1):
    count = 0
    case = input()
    for i in str(case):
        count += int(i)
        res = 0
        for j in range(2, 9):
            tmp = j*int(case)
            tmp_count = 0
            for k in str(case):
                tmp_count += int(k)
                if tmp_count == count:
                    res += 1
        if res > 0: 
            print("possible")
        else:
            print("impossible")
        res = 0            
        j = 0