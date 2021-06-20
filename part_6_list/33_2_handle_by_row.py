# 33.2 행 단위로 찾아 처리하기

import random
import math

r = 4
c = 5

lst = [ [None] * c for i in range(r) ]

for i in range(r):
    for j in range(c):

        lst[i][j] = random.randint(1, 20)


# 첫번째 방법 - 보조 리스트 만들기

sub_lst = [None] * r

for i in range(r):
    sub_lst[i] = 0

    for j in range(c):
        sub_lst[i] += lst[i][j]

    print("sub_lst:", sub_lst[i])



# 두번째 방법 - 파이썬 기능 이용해 보조 리스트 만들기
# The math.fsum() method returns the sum of all items in any iterable (tuples, arrays, lists, etc.).

sub_lst_2 = []

for i in lst:
    print("i:", i)
    print("math.fsum(i):", math.fsum(i))
    
    sub_lst_2.append(math.fsum(i))
    print("sub_lst_2:", sub_lst_2)



# 세번째 방법 - 해당 요소 찾아서 처리하기
# 내가 해결한 방법

for i in range(r):
    sum_row = 0

    for j in range(c):
        sum_row += lst[i][j]
        
        print("인덱스 값은", lst[i][j])
        print(i, "번째 행의 합은", sum_row)

    print(sum_row)


# 네번째 방법 - 파이썬 기능 이용해 요소 찾아 처리하기

total_row = 0
for row in lst:
    total_row = math.fsum(row)
    print("total_row:", total_row)
    



