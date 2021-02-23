# 20.3-2  파이썬 프로그램 줄이기

'''
다음 파이썬 프로그램을 더 적은 수의 명령문을 사용하여 재작성하여라.

a = int(input())

if a>0:
    y = a*4
    print(y)

else:
    y = a*3
    print(y)

'''

a = int(input())

if a > 0:
    y = a * 4

else:
    y = a * 3

print(y)



# 20.4-1  프로그래밍 코드 재작성하기

'''
다음 파이썬 프로그램을 논리 연산자를 사용하여 재작성하여라.

today = input()
name = input()

if today == "9.25":
    if name == "홍길동":
        print("Happy BirthDay!")
    else:
        print("No identified.")

else:
    print("No identified.")

'''

today = input()
name = input()

if today == "9.25" and name == "홍길동":
    print("Happy BirthDay!")

else:
    print("No identified.")


# 20.4-2  프로그래밍 코드 재작성하기

'''
다음 파이썬 프로그램을 논리 연산자를 사용하여 재작성하여라.

a = int(input())
b = int(input())

y = 0
if a > 10:
    y += 1
elif b > 20:
    y += 1
else:
    y -= 1

print(y)
'''

a = int(input())
b = int(input())

y = 0
if a > 10 or b > 20:
    y += 1

else:
    y -= 1

print(y)


# 20.5-1  결정 제어 구조 합치기

'''
다음 파이썬 프로그램에서 단일-택일 결정 구조들을 합쳐라.

a = int(input())

if a > 0:
    print("안녕하세요!")

if a > 0:
    print("반갑습니다.")

'''

a = int(input())

if a > 0:
    print("안녕하세요!")
    print("반갑습니다.")



# 20.5-2  결정 제어 구조 합치기

a = int(input())
b = int(input())

y = 0
if a > 0:
    y += 1
    print("안녕 철수")

a += 1
if a > 0:
    print('안녕 영희')

print(b)


# 20.6-1  결정 제어 구조 합치기

a = int(input())
b = int(input())

y = 0

if a > 0:
    y += 1

elif a <= 0:
    print("안녕 철수")

elif y > 0:
    print(y+5)

y += 1

if y <= 0:
    print(y + 12)