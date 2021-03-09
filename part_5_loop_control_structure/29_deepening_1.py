# 29.1-1  1+2+3+...+100 계산하기
S = 0
for i in range(1,101):
    S += i

print(S)


# 29.1-2  2*4*6*8*10 계산하기
P = 1
for i in range(2, 11, 2):
    P *= i

print(P)


# 29.1-3  2**2 + 4**2 + ... + (2N) ** 2 계산하기
S = 1
n = int(input("양의 정수를 입력하라"))
for i in range(2, 2*n+1, 2):
    S += i ** 2

print(S)


# 29.1-4  양수의 평균값 계산하기
nums = range(1, 200, 3)

total = 0
for i in nums:
    if i % 2 == 0:
        total += i

if total <= 0: 
    print("양수가 없습니다.")
else:
    print('양수의 평균값은', total / len(nums))


# 29.1-6  두 숫자의 대소 비교에 의한 개수 세기
from random import *

count_a = 0
count_b = 0

for i in range(10):
    a = randint(1, 100)
    b = randint(1, 100)

    if a > b:
        count_a += 1
        print(a, b)
    elif b > a:
        count_b += 1
        print(a, b)

print(count_a, count_b)


# 29.1-7  자릿수의 개수 세기
from random import *

count_1d = 0
count_2d = 0
count_3d = 0

for i in range(50):
    rdnum = randint(1, 999)

    if rdnum // 10 == 0:
        count_1d += 1
        print(rdnum, count_1d)
    elif rdnum // 10 <= 9:
        count_2d += 1
        print(rdnum, count_2d)
    else:
        count_3d += 1
        print(rdnum, count_3d)

print(count_1d, count_2d, count_3d)

     
# 29.1-8  숫자의 총합 구하기
# 입력받은 숫자의 총합이 1000을 초과할 때까지 숫자를 입력받고 숫자값의 총합을 출력하는 파이썬 프로그램을 작성하라.
sum_1000 = 0
count = 0

while sum_1000 <= 1000:
    rdnum2 = randint(1, 499)
    sum_1000 += rdnum2
    
    count += 1
    print(rdnum2, sum_1000)

print(sum_1000, count)


# 29.1-10  사용자가 원하는 횟수만큼 반복하기
count = 0

while True:
    first = randint(1, 100)
    second = randint(2, 9)
    result = first ** second
    count += 1
    print(result, first, second)

    answer = input("더 반복하시겠습니까?")
    if answer.upper() != "YES": break

print(result, count)



# 29.1-11  자릿수의 총합 계산하기
# code1 정수를 문자열로 바꾼 후, 다시 정수로 변경해 총합 계산
rdnum3 = str(int(input("정수를 입력하라")))
total = 0

for i in rdnum3:
    total += int(i)

print(total)

# code2 MOD 이용해 계산
rdnum4 = int(input("정수를 입력하라"))
total2 = 0

while rdnum4 != 0:
    a = renum4 % 10
    total2 += a
    renum4 = renum4 // 10

print(total2)


# 29.1-12  자릿수 세기
rdnum5 = int(input("정수를 입력하라"))
count_digit = 0

while True:
    rdnum5 = rdnum5 // 10
    count_digit += 1
    if rdnum5 == 0: break

print(count_digit)