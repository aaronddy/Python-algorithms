# 1. 더 적은 수의 명령문을 사용해 재작성하여라.

y = int(input("1. y 숫자를 입력하여라: "))
x = int(input("1. x 숫자를 입력하여라: "))

if y > 0:
    a = x * 4 * y + 1

else:
    a = x * 2 * y + 6

print("a", a)
print("y", y)



# 2. 다음 순서도를 더 적은 수의 명령문을 사용하여 재설계하여라.

x = float(input("2. x 숫자를 입력하여라: "))
y = x * 2

if x > 10:
    x = y * 300 - 6

else:
    x = y * 100 + 5

print("x", x)



# 3. 더 적은 수의 명령문을 사용하여 재작성하여라.

a = float(input("3. a 숫자를 입력하여라: "))

if a >= 10:
    print("오류!")

else:
    if a < 1:
        y = 5 + a

    elif a < 5:
        y = 23 / a

    elif a < 10:
        y = 5 * a

    print("y", y)



# 4. 논리 연산자를 사용해 재작성하여라.

day = int(input("4. 날짜 일을 입력하라: "))
month = int(input("4. 날짜 월을 입력하라: "))
name = input("4. 이름을 입력하라: ")

if day == 25 and month == 9 and name == "홍길동":
    print("Happy BirthDay!")

else: 
    print("No identified user.")



# 6. 단일-택일 결정 구조만을 사용해 재작성하여라.

a = float(input("6. 숫자를 입력하라: "))
b = float(input("6. 숫자를 입력하라: "))
c = float(input("6. 숫자를 입력하라: "))

if a > 10 and b < 2000 and c != 10:
    d = (a + b + c) / 12
    print("결과: ", d)

# a가 10 초과가 아닌 경우(a<=10인 경우)에 'error' 메시지를 따로 구분해서 띄워줘야 함. 단일-택일 결정 구조이므로 if 문을 추가 
if a <= 10:
    print("error!")


# 7. 단일-택일 결정 구조들을 합쳐라.

a = int(input("7. 숫자를 입력하라: "))
b = int(input("7. 숫자를 입력하라: "))

y = 3
if a > 0:
    y = y * a
    print("안녕 철슈!")

print(y, b)


# 8. 단일-택일 결정 구조들을 합쳐라. 

a = int(input("8. 숫자를 입력하라: "))
b = int(input("8. 숫자를 입력하라: "))

y = 0
if a > 0:
    y = y + 7

else:
    print("안녕 철슈")
    print(abs(a))

print(y)


# 9. 현재 가장 많이 사용되는 태블릿용 운영체제는 안드로이드, iOS, 윈도우 순이다. 불리언 식을 재배치하여 프로그램이 효율적으로 동작하도록 만들어라.

os = input("태블릿용 운영체제는 무엇인가요?")

if os == 'android':
    print("Google")

elif os == 'iOS':
    print("Apple")

elif os == 'window':
    print("Microsoft")


# 13. 정확한 들여쓰기를 사용하여 작성하여라. 그런 다음, 중첩 결정 제어 구조를 사용하여 프로그램을 재작성하여라.

a = float(input("13. 숫자를 입력하라: "))

if a >= 10:
    print("error!")

else: 
    if a < 1:
        y = 5 + a
    else:
        if a < 5:
            y = 23 / a
        else:
            if a < 10:
                y = 5 * a
    print(y)

