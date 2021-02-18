import math

# 제곱근 sqrt

x = float(input("type any number"))
y = math.sqrt(x)
print("x의 제곱근은", y)


# 정수 나눗셈 몫과 나머지

c, d = divmod(13, 4)
print(c, d, sep=', ')


# 정수값 반환

print(int(3))
print(int(39))
print(int(0.2))
print(int(-9.3))

a = "14"
b = "30"
print("문자열 concatanation ", a + b)
print("정수들의 합 ", int(a) + int(b))


# 실수값 변환

c = "5.9"
d = "10.4"

print(c + d)
print(float(c) + float(d))


# random
import random

print(random.randrange(2, 90))
print(random.randrange(-98, 5))
print(random.randrange(209495))


# fsum : sequence에 있는 원소값들의 총합 반환

seq = [20, 1, 0.9, 4, -20]
print(math.fsum(seq))



# 예제 1

x = float(input("type X"))

x += 6 / math.sqrt(x) * 2 + 20
y = round(x) % 4
z = y % 3

print(x, y, z, sep=', ')


# 예제 2

m = int(input())
n = abs(m) % 4 + m ** 4
p = n % 5

print(n, p, sep=", ")