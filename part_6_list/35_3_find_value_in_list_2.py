# 35.3-5 2차원 리스트에서 가장 큰 값 찾기
# 10개 도시의 1월 한 달간 정오 온도를 입력하고 가장 낮은 온도를 출력하라. 

import random
import math

CITIES = 10
DAYS = 31

temp_jan = [ [None] * DAYS for i in range(CITIES) ]

for i in range(CITIES):
    for j in range(DAYS):
        temp_jan[i][j] = random.randint(-25, 25)

print("temp_jan:", temp_jan)

# 방법 A
min_temp = 100
city = -1
day = -1

for i in range(CITIES):
    for j in range(DAYS):
        if temp_jan[i][j] <= min_temp:
            min_temp = temp_jan[i][j]
            city = i
            day = j

print("가장 낮은 온도는", min_temp, "도시 넘버는", city+1, "번째, 날짜는 1월", day+1)

# 방법 B
min_temp_2 = 100

for i in range(CITIES):
    if min(temp_jan[i]) <= min_temp_2:
        min_temp_2 = min(temp_jan[i])

print("가장 낮은 온도는", min_temp_2)



# 35.3-6  가장 추웠던 도시 찾기
cities_name = ['Seoul', 'Busan', 'Ulsan', 'Gwangju', 'Incheon', 'Dokdo', 'Suwon', 'Daejeon', 'Jeonju', 'Jeju']

min_temp3 = 1000
k_city = -1
k_day = -1

for i in range(CITIES):
    for j in range(DAYS):
        if temp_jan[i][j] <= min_temp3:
            min_temp3 = temp_jan[i][j]
            k_city = i
            k_day = j

print("가장 낮은 온도는", min_temp3, "도시 이름은", cities_name[k_city], "날짜는 1월", k_day+1)



# 35.3-7  각 행의 최솟값과 최댓값 찾기
ROWS = 20
COLUMNS = 30

lst = [ [None] * COLUMNS for i in range(ROWS) ]

for i in range(ROWS):
    for j in range(COLUMNS):
        lst[i][j] = random.randint(0, 2000)

# 방법 A - 보조 리스트 만들기
mini_lst = []
max_lst = []

for i in range(ROWS):
    minimum = lst[i][0]
    maximum = lst[i][0]

    for j in range(1, COLUMNS):
        if lst[i][j] < minimum:
            minimum = lst[i][j]
        
        if lst[i][j] > maximum:
            maximum = lst[i][j]
        
    mini_lst.append(minimum)
    max_lst.append(maximum)

print("mini_lst:", mini_lst)
print("max_lst:", max_lst)


# 방법 B - 최솟값과 최댓값 찾아 바로 출력하기
for i in range(ROWS):
    minimum2 = lst[i][0]
    maximum2 = lst[i][0]

    for j in range(1,COLUMNS):
        if lst[i][j] < minimum2:
            minimum2 = lst[i][j]

        if lst[i][j] > maximum2:
            maximum2 = lst[i][j]


    print("minimum:", minimum2)
    print("maximum:", maximum2)    


# 방법 C - 파이썬다운 방식
for i in lst:
    print("min:", min(i))
    print("max:", max(i))

print("**********************************")

# 35.3-8  각 열의 최솟값과 최댓값 찾기

lst2 = [ [None] * COLUMNS for i in range(ROWS) ]

for i in range(ROWS):
    for j in range(COLUMNS):
        lst2[i][j] = random.randint(0, 2000)

# 방법 A - 보조 리스트 만들기
mini_lst2 = []
max_lst2 = []

for j in range(COLUMNS):
    c_mini = lst2[0][j]
    c_max = lst2[0][j]

    for i in range(1, ROWS):
        if lst2[i][j] < c_mini:
            c_mini = lst2[i][j]

        if lst2[i][j] > c_max:
            c_max = lst2[i][j]

    mini_lst2.append(c_mini)
    max_lst2.append(c_max)

for j in range(COLUMNS):
    print(mini_lst2[j], max_lst2[j])