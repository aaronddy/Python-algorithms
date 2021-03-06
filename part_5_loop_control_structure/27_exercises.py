# 1. 다음 코드는 사용자가 입력한 100개의 숫자들에 대한 평균값을 계산한다. 가능한 많은 명령문을 루프 외부로 이동하여 코드를 효율적으로 만들어라.
s = 0
for i in range(100):
    number = float(input())
    s = s + number

average = s / 100     # average는 총합 s를 100으로 나누면 되므로 루프 외부로 이동
print(average)


# 2. 방정식의 해를 구하는 파이썬 프로그램이 있다. 가능한 많은 명령문을 루프 외부로 이동하여 프로그램을 효율적으로 만들어라.
s = 0
denom = 1   # 상수를 변수에 입력하므로 루프 외부로 이동

for j in range(1, 101):    # 각 for loop의 변수들이 서로 영향을 주고 받지 않기 때문에 각각의 for loop으로 분리시키면 더 효율적으로 코드를 작동시킬 수 있다.
    denom *= j

for i in range(1, 101):
    s += i / denom

print(s)


# 3. 다음 코드를 while loop을 사용해 재작성하라.
import math
s = 10
i = 1

while i < 11:
    s += math.sqrt(i)
    i += 1

print(s)


# 4. 다음 코드를 while loop을 사용해 재작성하라.
start = int(input())
finish = int(input())
i = start

while i < finish + 1:
    print(i)
    i += 1


# 5. 다음 코드를 while loop을 사용해 재작성하라.
start = int(input())
i = start
x = 1

while i < start * 2 + 1:
    x = x ** 1.1 + i
    i += 1

print(i)


# 6. 다음 코드를 while loop을 사용해 재작성하라.
x = 42
i = 0

while i < 100:
    x = math.sqrt(x) + i
    print(x)
    i += 1


# 7. 다음 코드를 for loop을 사용해 재작성하라.
s = 0

for i in range(100, 0, -5):
    s = s + math.sqrt(i)

print(s)


# 8. 다음 코드를 for loop을 사용해 재작성하라.
s = 0
y = 0

for i in range(4, 23, 3):
    s = s + math.sqrt(y + i)
    y = y + i * 2

print(s)


# 9. 다음 코드를 for loop을 사용해 재작성하라.
y = 0

for i in range(1, 10, 2):
    a = float(input())
    a += i
    y = y + (a + i + 2) ** 3

print(y)


# 12. 다음 코드를 for loop을 사용해 재작성하라.
x = 0

for y in range(-10, 10):
    x = x + 2 ** y

print(x)


