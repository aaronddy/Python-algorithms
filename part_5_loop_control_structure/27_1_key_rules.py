# 다섯 개의 숫자를 입력받고, 그 숫자들 중 짝수의 총 개수와 홀수의 총 개수를 출력하는 파이썬 프로그램을 작성하라.

odd = 0
even = 0

for i in range(5):
    x = int(input("숫자를 입력하시오:"))

    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("홀수:", odd, "짝수:", even)


# 27.7-1  파이썬 프로그램 변환하기(1)
# while loop를 사용해 프로그램을 작성하라.

s = 'Hello'
for letter in s:
    print(letter)

i = 0
while i < len(s):
    print(s[i])
    i += 1


# 27.7-2  파이썬 프로그램 변환하기(2)
# while loop을 사용해 프로그램을 재작성하라.

x = 2

for i in range(-2, 3):
    x = x ** 2

print(x)

i = -2
while i < 3:
    x = x ** 2
    i += 1

print(x) 


# 27.7-3  파이썬 프로그램 변환하기(3)
# 사전-검사 루프 구조를 사용해 재작성하라.

f = int(input())
x = 3

for j in range(20, f, -5):
    x = x / 2

print(x, j)

j = 20
while j > f:
    x = x / 2
    j -= 5

j += 5
print(x, j)
