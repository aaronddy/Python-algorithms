# 35.4-1  버블 정렬 알고리즘 - 숫자값을 가지는 1차원 리스트 정렬하기

import random

SIZE = 8
bub_lst = [None] * SIZE   

for i in range(SIZE):
    bub_lst[i] = random.randint(1, 50)

print("bub_lst:", bub_lst)

m = 0
while m < SIZE-1:
    for i in range(SIZE-1, m, -1):
        if bub_lst[i] < bub_lst[i-1]:
            bub_lst[i], bub_lst[i-1] = bub_lst[i-1], bub_lst[i]
    
    print("bubbling:", bub_lst)
    m += 1
    print("m:", m)

print("bub_lst_sorted:", bub_lst)


# 35.4-2  영숫자값을 가진 1차원 리스트 정렬하기
# 버블 정렬 알고리즘을 사용하여 영숫자값을 요소로 가진 리스트를 내림차순으로 정렬하는 파이썬 프로그램을 작성하라.

words = ['flower', 'youtube0', 'poppy', '132tower', 'squads', 'main', 'youth']
W_SIZE = len(words)

w = 0
while w < W_SIZE-1:
    for i in range(W_SIZE-1, w, -1):
        if words[i] < words[i-1]:
            words[i], words[i-1] = words[i-1], words[i]
    
    print("words_bubbling:", words)
    w += 1

print("bub_words:", words)



# 35.4-3  두 번째 리스트와의 관계를 유지하면서 1차원 리스트 정렬하기
# 20개의 호수 이름과 길이 리스트를 생성하고, 버블 정렬 알고리즘을 사용해 호수의 길이를 기준으로 오름차순 정렬한다.

lakes = ['Caspian Sea', 'Superior', 'Victoria', 'Huron', 'Michigan', 'Tanganyika', 'Baikal', 'Great Beark Lake', 'Malawi', 'Great Slave Lake', 'Erie', 'Winnipeg', 'Ontario', 'Ladoga', 'Balkhash', 'Bangweulu', 'Vostok', 'Onega', 'Titicaca', 'Nicaragua']
lengths = [1199, 616, 322, 332, 494, 676, 636, 373, 579, 480, 388, 425, 311, 219, 605, 75, 250, 245, 177, 180]

L_SIZE = len(lakes)
L = 0

while L < L_SIZE - 1:
    for i in range(L_SIZE-1, L, -1):
        if lengths[i] < lengths[i-1]:
            lengths[i], lengths[i-1] = lengths[i-1], lengths[i]
            lakes[i], lakes[i-1] = lakes[i-1], lakes[i]

    L += 1

print("sorted_lakes:", lakes)



# 35.4-4  2차원 리스트 정렬하기
# 2차원 리스트의 각 열을 오름차순으로 정렬하는 파이썬 프로그램을 작성하라. 단 이 리스트는 숫자값만을 가진다.

ROWS = 6
COLUMNS = 4

lst = [ [None] * COLUMNS for i in range(ROWS) ]

for i in range(ROWS):
    for j in range(COLUMNS):
        lst[i][j] = random.randint(1, 99)


for j in range(COLUMNS):
    
    # r 초기화하고 각 열의 행 순서대로 버블 정렬 진행
    r = 0
    while r < ROWS-1: 
        for i in range(ROWS-1, r, -1):
            if lst[i][j] < lst[i-1][j]:
                lst[i][j], lst[i-1][j] = lst[i-1][j], lst[i][j]
        
        r += 1 

print("lst:", lst)
