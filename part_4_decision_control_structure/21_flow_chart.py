# 21.3-1  파이썬 프로그램 작성하기

x = float(input())
y = 50

if x / 2 <= 10:
    x = x / 3
    y = x + 4

print(y)



# 21.3-2  파이썬 프로그램 작성하기

x = float(input())
y = 1

if x != 100:

    y = float(input())

    if x < y:
        x = x-3
        y = x+4
    
    else:
        x = x/3 + 5
        y = x+20

print(x, y)



# 21.3-3  파이썬 프로그램 작성하기

x = float(input())
y = float(input())

# code1
if x % y != 1:
    
    if y % 1 != 1:
        print("부적절함")

    else:
        a = 20
        print(a)

else:
    a = 10
    print(a)


# code2
if x % y == 1:
    a = 10
    print(a)

elif y % x == 1:
    a = 20
    print(a)

else:
    print('부적잘')



# 21.3-4  파이썬 프로그램 작성하기

x = float(input())
y = float(input())

if x % y != 1:
    print("안녕")
    a = 1
elif y % x != 1:
    a = 1
else:
    a = 2

print(a)


# 21.3-5  파이썬 프로그램 작성하기

a = float(input())
b = float(input())
c = a % 2
d = b // 5

if a >= b:
    y = 1
elif d > c and a > 2:
    y = 2
elif d * c > a / b:
    if d * c > 10:
        y = 4
    else:
        y = 3
else:
    y = 5

print(y)