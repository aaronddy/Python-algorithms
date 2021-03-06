# 27.8-1  파이썬 프로그램 변환하기(1)
# for loop을 사용해 재작성하라.

# while loop
s = 0
i = 1
while i <= 9:
    s = s + i ** 2
    i += 2

print(s)

# for loop 
s = 0

for i in range(1, 10, 2):
    s = s + i ** 2

print(s)


# 27.8-2  파이썬 프로그램 변환하기(2)
# for loop을 사용해 재작성하라.

# while loop
s = 0
y = 5

while y != -3:
    s = s + 2 * y
    y = y - 2

print(s)

# for loop
s = 0

for i in range(5, -3, -2):
    s = s + 2 * y

print(s)


# 27.8-3  파이썬 프로그램 변환하기(3)
# for loop을 사용해 재작성하라.

# while loop
s = 0
i = 1

while i < 6:
    i += 1
    s = s + i ** 2

print(s)

# for loop
s = 0

for i in range(1, 6):
    s = s + (i + 1) ** 2

print(s)


# 27.8-5  파이썬 프로그램 변환하기(5)
# for loop을 사용해 재작성하라.

# while loop
s = 0
y = 5

while y > -9:
    s = s - 2 + y
    y = y - 3
    s = s - 4 * y

print(s)

# for loop
s = 0

for y in range(5, -9, -3):
    s = s - 2 + y
    y = y - 3
    s = s - 4 * y

print(s)


