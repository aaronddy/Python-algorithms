# 28.3-1  파이썬 프로그램 작성하기

i = 1
while i <= 90:
    print(i)
    i += 2

print("끝")


# 28.3-2  파이썬 프로그램 작성하기

i = 1
while True:
    if i < 45:
        print(i)
    else:
        print(-i)

    i += 1
    if i >= 90: break

print("끝")


# 28.3-3  파이썬 프로그램 작성하기

s = 0
i = 0

while i <= 99:
    while True:                  # 사후-검사 루프 구조
        n = float(input())
        if n >= 0: break

    if n < 100:                  # 이중-택일 결정 구조
        s = s + n ** 2
    else:
        s = s + n ** 3
    i += 1
    
print(s)


# 28.3-4  파이썬 프로그램 작성하기

i = 0
s = 0

while True:
    a = float(input())
    i += 1
    
    if i >= 90: break
    
    s = s + a * i

print(s)