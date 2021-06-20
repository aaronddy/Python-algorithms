
# n * n 리스트 생성
import random

n = 8
list_8 = [ [None] * 8 for i  in range(n) ]

for i in range(n):
    for j in range(n):
        list_8[i][j] = random.randint(1, 100)

# print(list_8)

# 9. 홀수의 값을 가지고 있는 요소의 인덱스를 출력하는 프로그램을 작성하라.

counter_odd = 0

for i in range(n):
    for j in range(n):

        if list_8[i][j] % 2 == 1:
            print("i:", i, ", j:", j, ", value:", list_8[i][j])
            counter_odd += 1

print("total_counter_odds:", counter_odd)



# 10. 짝수의 값을 가지고 있는 요소의 인덱스를 출력하는 프로그램을 작성하라.

counter_even = 0

for i in range(n):
    for j in range(n):

        if list_8[i][j] % 2 == 0:

            print("i:", i, ", j:", j, ", value:", list_8[i][j])
            counter_even += 1

print("total_counter_even:", counter_even)



# 11. 짝수의 값과 홀수의 값을 가진 요소들의 합을 계산하고 출력하는 프로그램을 작성하라.

sum_odds = 0
sum_evens = 0

for i in range(n):
    for j in range(n):

        if list_8[i][j] % 2 == 1:
            sum_odds += list_8[i][j]

        else:
            sum_evens += list_8[i][j]

print("odds:", sum_odds)
print("evens:", sum_evens)



# 12. 정사각형 리스트의 대각선에 있는 요소들의 평균값과 역대각선에 있는 요소들의 평균값을 각각 계산하는 프로그램을 작성하라.

sum_cross = 0
sum_reverse = 0

for i in range(n):
    for j in range(n):

        if i == j:
            sum_cross += list_8[i][j]
            # print("index:", i, j)

        elif i + j == n - 1:
            sum_reverse += list_8[i][j]
            # print("index:", i, j)

print("sum_cross:", sum_cross)
print("sum_reverse:", sum_reverse)
print("mean_cross:", sum_cross / n)
print("mean_reverse:", sum_reverse / n)


sum_cross_2 = 0
sum_reverse_2 = 0

for i in range(n):

    sum_cross_2 += list_8[i][i]
    sum_reverse_2 += list_8[i][n-i-1]

print("sum_cross_2:", sum_cross_2)
print("sum_reverse_2:", sum_reverse_2)
print("mean_cross_2:", sum_cross_2 / n)
print("mean_reverse_2:", sum_reverse_2 / n)



