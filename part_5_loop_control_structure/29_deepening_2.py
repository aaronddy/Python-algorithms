# 29.2-1  세 자리의 정수 출력하기
# 한 자릿수 정수(0-9)를 입력받고 그 정수가 최소 한 번 이상 포함된 세 자릿수 정수를 출력하는 프로그램을 작성하라.

import random

x = int(input("0-9 중 한 자리수 정수를 입력하라"))

randint = random.randint(100, 999)

if str(x) in list(str(randint)):
    print("if", randint)
else:
    randint = str(randint).replace(str(randint)[1], str(x))
    print("else", randint)


# 29.2-2  특정 조건에 따라 출력하기
# 첫 번째 자릿수값이 두 번째 자릿수값보다 작고, 두 번째 자릿수값이 세 번째 자릿수보다 작은 조건을 가진 세 자릿수 정수를 출력하는 프로그램을 작성하라.

digit1 = random.randint(1, 7)
digit2 = random.randint(digit1+1, 8)
digit3 = random.randint(digit2+1, 9)
randnum = digit1 * 100 + digit2 * 10 + digit3
print(randnum)


