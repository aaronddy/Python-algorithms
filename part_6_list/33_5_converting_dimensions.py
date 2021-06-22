# 33.5 2차원 리스트로부터 1차원 리스트 만들기
# 3 * 4 크기의 2차원 리스트로부터 12개의 요소를 가지는 2차원 리스트를 만드느 프로그램을 작성하라.

import random

ROWS = 3
COLUMNS = 4

lst = [ [None] * COLUMNS for i in range(ROWS) ]

for j in range(COLUMNS):
    for i in range(ROWS):
        lst[i][j] = random.randint(1, 30)

print("lst:", lst)

k = 0
to_lst = [None] * ROWS * COLUMNS

for j in range(COLUMNS):
    for i in range(ROWS):
        to_lst[k] = lst[i][j]
        k += 1
        
print("to_lst:", to_lst)



# 33.6 1차원 리스트로부터 2차원 리스트 만들기
# 12개 요소를 가지는 1차원 리스트로부터 2 * 6 크기의 2차원 리스트를 만드는 프로그램을 작성하라.

ROWS = 2
COLUMNS = 6

t = 0
to_one = [ [None] * COLUMNS for i in range(ROWS) ]

for j in range(COLUMNS):
    for i in range(ROWS):

        to_one[i][j] = to_lst[t]
        t += 1

print("to_one:", to_one)
