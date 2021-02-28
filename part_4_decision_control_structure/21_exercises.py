# 6. 다음 순서도에 대한 파이썬 프로그램을 작성하라.

x = float(input())
y = float(input())

if not(x == 10 and y > 10):
    z = float(input())

    if z <= x + y:
        x = x - 3
        y = x + 4
    
print(x,y)


# 7. 다음 순서도에 대한 파이썬 프로그램을 작성하라.

x = float(input())

if x == 1:
    print("좋은 아침!")
    print("안녕하세요?")
    print("별일 없으시죠?")    

elif x == 2:
    print("즐거운 저녁")
    print("안녕하세요?")
    print("별일 없으시죠?"
    )
elif x == 3:
    print("좋은 오후")
    print("별일 없으시죠?")

else:
    print("안녕히 주무세요.")



# 8. 다음 순서도에 대한 파이썬 프로그램을 작성하라.

import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

x = input()
if re.match(IS_NUMERIC, x):
    x = int(x)
    if x % 10 == 0:
        print("마지막 자릿수는 0입니다.")
    elif x % 10 == 1:
        print("마지막 자릿수는 1입니다.")
    else:
        print("특별하지 않네요")

else:

    if x == "Exit":
        print("끝")
    else:
        print("올바르지 않은 수입니다.")



# 9. 다음 순서도에 대한 파이썬 프로그램을 작성하라.

a = float(input())
b = float(input())

y = a * b

if y > 0:
    y = y-1
    y = y/2
else:
    y = y+10
    if y > 0:
        y = y/2
    else:
        y = y*2



# 10. 다음 순서도에 대한 파이썬 프로그램을 작성하라.

a = float(input())
b = float(input())
c = float(input())

c = a * b + c

if c > 0:
    c = c / 2

    if a > b:
        a = a * 2
        b = b * 2
    else:
        c = c / 20
        if c <= 10:
            b = b * 2
else:
    c = c / 3
    c = c / 20
    if c <= 10:
        b = b * 2

print(a, b, c)
