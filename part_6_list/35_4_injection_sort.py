# 35.4-10  삽입 정렬 알고리즘 - 1차원 리스트 정렬하기

import random

SIZE = 10
lst = [None] * SIZE

for i in range(SIZE):
    lst[i] = random.randint(1, 50)

print("lst:", lst)

for m in range(1, SIZE):
    element = lst[m]
 
    for n in range(m, 0, -1):
        if element < lst[n-1]:
            lst[n], lst[n-1] = lst[n-1], element 
    
print("final_lst:", lst)


# 35.4-11  세 개의 가장 오래 걸린 경과 시간

TIMES = 20
players = ['Smith', 'Jones', 'Williams', 'Taylor', 'Brown', 'Davies', 'Evans', 'Wilson', 'Thomas', 'Johnson']
e_times = [[None] * TIMES for i in range(SIZE) ]

for i in range(SIZE):
    for j in range(TIMES):
        e_times[i][j] = random.randint(50, 200)
print("e_times:", e_times)

for i in range(SIZE):
    for j in range(1, TIMES):
        time = e_times[i][j]

        for n in range(j, 0, -1):
            if time < e_times[i][n-1]:
                e_times[i][n], e_times[i][n-1] = e_times[i][n-1], time
        
print("final_e_times:", e_times)

for i in range(SIZE):
    print(players[i], "선수의 가장 오래 걸린 시간은", e_times[i][TIMES-1], e_times[i][TIMES-2], e_times[i][TIMES-3], "입니다.")