# 35.1-1 이웃 요소의 평균값을 가지는 리스트 만들기

import random

ELEMENTS_OF_A = 20
ELEMENTS_OF_NEW = ELEMENTS_OF_A - 2

a = [None] * ELEMENTS_OF_A
new = [None] * ELEMENTS_OF_NEW

for i in range(ELEMENTS_OF_A):
    a[i] = random.randint(0, 20)

print("a_lst:", a)

# 방법 A
for j in range(ELEMENTS_OF_NEW):
    sum_a = a[j] + a[j+1] + a[j+2]
    new[j] = round(sum_a / 3, 2)

print("new_a_lst:", new)


# 방법 B
import math

new_lst = []
for k in range(ELEMENTS_OF_A - 2):
    new_lst.append(math.fsum(a[k:k+3]) / 3)

print("new_lst:", new_lst)




# 35.1-2 최댓값을 저장하는 리스트 만들기

ELEMENTS_M_N = 20

m = [None] * ELEMENTS_M_N
n = [None] * ELEMENTS_M_N

for i in range(ELEMENTS_M_N):
    m[i] = random.randint(1, 30)
    n[i] = random.randint(1, 30)

print("m_lst:", m)
print("n_lst:", n)

new_arr = []
for j in range(ELEMENTS_M_N):
    max_value = max(m[j], n[j])
    new_arr.append(max_value)

print("new_arr:", new_arr)



# 35.1-3 1차원 리스트 병합하기

ELEMENTS_A = 12
ELEMENTS_B = 13

lst_a = [None] * ELEMENTS_A
lst_b = [None] * ELEMENTS_B

for i in range(ELEMENTS_A):
    lst_a[i] = random.randint(1, 10)

for j in range(ELEMENTS_B):
    lst_b[j] = random.randint(1, 10)

new_arrA = [None] * (ELEMENTS_A + ELEMENTS_B)

# 방법 A
for k in range(ELEMENTS_A + ELEMENTS_B):
    
    if k < ELEMENTS_A:
        new_arrA[k] = lst_a[k]
    else:
        new_arrA[k] = lst_b[k-ELEMENTS_A]
    
print("lst_a:", lst_a)
print("lst_b:", lst_b)
print("new_arrA:", new_arrA)


# 방법 B
new_arrB = lst_a + lst_b
print("new_arrB:", new_arrB)


# 방법 C
new_arrC = []

for i in range(ELEMENTS_A):
    new_arrC.append(lst_a[i])

for i in range(ELEMENTS_B):
    new_arrC.append(lst_b[i])

print("new_arrC:", new_arrC)