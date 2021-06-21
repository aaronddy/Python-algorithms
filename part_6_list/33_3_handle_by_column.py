# 33.3 열 단위로 처리하기

import random

r = 4
c = 5
lst = [ [None] * c for i in range(r) ]

for i in range(r):
    for j in range(c):
        lst[i][j] = random.randint(1, 25)

print("lst:", lst)


# 첫번째 방법 - 보조 리스트 만들기

sub_lst = [None] * c

for i in range(c):
    sub_lst[i] = 0

    for j in range(r):
        sub_lst[i] += lst[j][i]
        print("index:", lst[j][i], "sum_col", sub_lst[i])

    print("sub_lst:", sub_lst)



# 두번째 방법 - 해당 요소 찾아서 처리하기

for j in range(c):
    sum_col = 0

    for i in range(r):
        sum_col += lst[i][j]
        print("index:", lst[i][j], "sum_col:", sum_col)
    
    print("sum_col:", sum_col)