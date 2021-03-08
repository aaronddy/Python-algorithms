# 13. 다음 순서도에 대한 파이썬 프로그램을 작성하라.

i = 1
while True:
    i = float(input())
    i += 5
    if i > 500: break

print("end")


# 14. 다음 순서도에 대한 파이썬 프로그램을 작성하라.

i = 0
a = float(input())

while True:
    if i % 2 != 0:
        print(i)
    i = i + 5
    if i >= a: break


# 15. 다음 순서도에 대한 파이썬 프로그램을 작성하라.

a = int(input())

if a != -1:
    while True:
        b = int(input())
        if b > a: break
    i = a
    while i <= b:
        print(i)
        i = i + 1
    a = float((input()))
    

# 16. 다음 순서도에 대한 파이썬 프로그램을 작성하라.

i = 1
S = 0
P = 1
a = 0

while True:
    if i < 45:
        S += a
    else:
        P *= a

    i += 1

    if i < 90: break
    a = float(input())

print(S,P)