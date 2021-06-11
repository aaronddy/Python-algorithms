# 32.6 정방 행렬

# 32.6-1 대각선 요소들의 합 구하기
import random

n = 7
n_list = [ [None] * n for i in range(n) ]

for i in range(n):
    for j in range(n):
        n_list[i][j] = random.randint(1, 20)

print("n_list:", n_list)

# 정방 행렬 대각선 요소 합 구하기
tot_sum = 0
for k in range(n): 
    tot_sum += n_list[k][k] 
    print(tot_sum, n_list[k][k])

print("tot_sum:", tot_sum)


# 32.6-2 역대각선 요소들의 합 구하기

m = 7
m_list = [ [None] * m for i in range(m) ]

for i in range(m):
    for j in range(m):
        m_list[i][j] = random.randint(1, 20)

print("m_list:", m_list)


# 역대각선 요소들의 합 구하기
tot_sum2 = 0
for i in range(m):
    j = m-i-1
    tot_sum2 += m_list[i][j]
    print(tot_sum2, m_list[i][j])

print("tot_sum2:", tot_sum2)



# 32.6-3 리스트 채우기

num = 5
a_list = [ [None] * num for i in range(5) ]

for i in range(num):
    for j in range(num):

        if i == j:
            a_list[i][j] = -1
        elif i < j:
            a_list[i][j] = 20
        else:
            a_list[i][j] = 10

print("a_list:", a_list)