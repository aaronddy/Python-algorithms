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



# 20.8-1  다중-택일 결정 구조를 중첩 결정 구조로 바꾸기

x = float(input("첫 번째 숫자를 입력하라: "))
y = float(input("두 번째 숫자를 입력하라: "))

result = x * y

if x < 0 and y < 0:
    print("두 음수의 곱은 양수입니다.")
    print(x, "* (", y, ")의 값: +", result, sep="")

else:
    if x < 0:
        print("음수와 양수의 곱은 음수입니다.")
        print(x, "* ", y, "의 값: +", result, sep="")


    else:
        if y < 0:
            print("음수와 양수의 곱은 음수입니다.")
            print(x, "* (", y, ")의 값: +", result, sep="")

        else:
            print("두 양수의 곱은 양수입니다.")
            print(x, "* ", y, "의 값: +", result, sep="")



# 20.9  결정 제어 구조에서 '내부에서 외부로' 방식 사용하기

num9 = input("하나의 정수값을 입력하라")


if not int(num9):
    
    pass

else:

    remain = int(num9) % 10 

    if remain == 5:
        print("마지막 자릿수값은 5입니다.")

    else:
        print("특별한 것이 없네요.")