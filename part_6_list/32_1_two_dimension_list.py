# 32.4 2차원 리스트에 반복 처리 사용하기

# 행에 따라 반복하기

deer_cafe = [ [None] * 3 for i in range(2) ]
print(deer_cafe)

deer_cafe[0] = ["Americano", "Latte", "Lemon ade"]
deer_cafe[1] = ["Scone", "Brownie", "Cheese cake"]

for i in range(2):
    for j in range(3):
        print(deer_cafe[i][j], end='\t')
    print()


# 열에 따라 반복하기

test_a = [[0, 3, 4, 4], [2, 3, 1, 0], [5, 7, 3, 10]]

j = 0
for i in range(3):
    print(test_a[i][j])

j = 1
for i in range(3):
    print(test_a[i][j])

j = 2
for i in range(3):
    print(test_a[i][j])

j = 3
for i in range(3):
    print(test_a[i][j])


for j in range(4):
    for i in range(3):
        print(test_a[i][j], end='\t')
    print()


# 32.4-1 조건에 맞는 숫자들만 출력하기
import random

rows = 5
columns = 7

test_b = [ [None] * columns for i in range(rows) ]

for i in range(rows):
    for j in range(columns):
        test_b[i][j] = random.randint(10, 30)
    
print("test_b:", test_b)

counter = 0
for i in range(rows):
    for j in range(columns):
        if test_b[i][j] < 15:
            counter += 1
            print(i, ",", j, "위치에서 15보다 적은 정수가 발견되었습니다.")

print("총", counter, "개 입니다.")


# 32.4-2 인덱스가 홀수인 열들만 출력하기
for j in range(1, columns, 2):
    for i in range(rows):
        print(test_b[i][j], i, j)