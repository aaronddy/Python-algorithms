# 35.1-5  두 개 리스트 만들기 - 양수와 음수 분리하기

import random

lst = []
size = 100

for i in range(size):
    lst.append(random.randint(-100, 100))

print("lst:", lst)

# 방법 A
pos_A = []
negs_A = []

for i in range(size):
    if lst[i] > 0:
        pos_A.append(lst[i])

    elif lst[i] < 0:
        negs_A.append(lst[i])

print("pos_A:", pos_A)
print("negs_A:", negs_A)


# 방법 B
cnt_pos = 0
cnt_negs = 0

for i in range(size):
    if lst[i] > 0:
        cnt_pos += 1
    
    elif lst[i] < 0:
        cnt_negs += 1

pos_B = [None] * cnt_pos
negs_B = [None] * cnt_negs

pos_index = 0
negs_index = 0

for i in range(size):
    if lst[i] > 0:
        pos_B[pos_index] = lst[i]
        pos_index += 1

    elif lst[i] < 0:
        negs_B[negs_index] = lst[i]
        negs_index += 1

print("pos_B:", pos_B)
print("negs_B:", negs_B)




# 35.1-6  5 값을 갖고 있는 숫자들의 리스트 만들기

rdn_lst = [None] * size
for i in range(size):
    rdn_lst[i] = random.randint(10, 99)

print("rdn_lst:", rdn_lst)

includings = []

for i in range(size):
    if rdn_lst[i] // 10 == 5 or rdn_lst[i] % 10 == 5:
        includings.append(rdn_lst[i])

print("includings:", includings)