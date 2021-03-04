# file_25_1a

for i in [1, 2, 3, 4, 5]:
    print(i)

for letter in "Hello":
    print(letter)


# ragne() 함수는 연속적인 정수를 생성하는 데 사용.
# 0 - 10 차례대로 출력
for i in range(11):
    print(i)

# 10 - 2까지의 짝수를 차례대로 출력
for i in range(10, 1, -2):
    print(i)


# 25.1-4  10개 숫자의 총합 계산하기
# code 1
total = 0
i = 0

while i < 10:
    num = float(input("숫자를 입력하쇼:"))
    total += num
    i += 1
    # print("i", i)
print("total", total)

# code 2
total2 = 0

for i in range(10):
    num2 = float(input("숫자를 입력하슈:"))
    total2 += num2

print(total2)


# 25.1-5  0부터 N까지 제곱근 계산하기
# N개 정수를 입력받은 후 0부터 N까지의 제곱근을 각각 계산하고 출력하는 프로그램을 작성하라.
import math

int_N = int(input("n을 입력하라:"))
sum_sqrt = 0

for i in range(int_N+1):
    sqrt = math.sqrt(i)
    sum_sqrt += sqrt

print(sum_sqrt)


# 25.2-1  N개 숫자의 평균 계산하기
n = int(input("n을 입력하라:"))

total3 = 0
for i in range(n):
    num3 = int(input("정수를 입력하여라"))
    total3 += num3

if n > 0:
    avg = total3 / n
    print("평균:", avg)
else:
    print("입력된 정수가 없습니다.")