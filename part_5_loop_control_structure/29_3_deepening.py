# 29.3 루프 제어 구조의 데이터 유효성: 데이터 유효성은 사용자에게 유효한 값만을 입력하도록 함으로써 데이터 입력을 제한하는 과정이다.

import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input('숫자를 입력하여라: ')

if re.match(IS_NUMERIC, inp):
    print(inp, "숫자입니다")
else:
    print("숫자를 입력하지 않았습니다.")

'''
위 방법은 데이터 유효성 검사를 할 수 있으나, 최선의 방법은 아니다. 그 이유는 유효하지 않은 숫자를 사용자가 입력하면 위 프로그램은 오류 메시지를 출력하고 어쩔 수 없이 수행을 종료하기 때문이다.
사용자가 유효하지 않은 값을 계속 입력하면 유효한 값을 입력할 때까지 반복하여 입력하게 하는 것이 핵심 아이디어다. 
'''
print('=======================')

# 29.3-1  제곱근 계산하기 - 오류 메시지 출력이 없는 유효성 검사
# 숫자값을 입력받고 그 숫자값의 제곱근을 계산하는 프로그램을 작성하라. 음수가 아닌 숫자값만을 입력받도록 데이터 입력의 유효성을 검사해야 한다. 오류 메시지는 출력하지 않는다.

# 데이터 입력의 유효성 검사를 고려하지 않은 프로그램
import math

x = float(input("숫자를 입력하여라"))

sqrt_x = math.sqrt(x)
print(sqrt_x)


# 데이터 입력의 유효성을 검사하는 프로그램
IS_NUMERIC = "^[+]?\\d+(\\.\\d+)?$"

while True:
    inp = input("양의 실수를 입력하라")
    if re.match(IS_NUMERIC, inp): break
    
num = float(inp)
num = math.sqrt(num)
print(round(num,2))


# 29.3-2  제곱근 계산하기 = 하나의 오류 메시지를 이용한 유효성 검사
# 음수가 아닌 숫자값만을 입력받도록 데이터 입력의 유효성을 검사해야 하며, 음수가 아닌 숫자값을 입력했을 때 하나의 오류 메시지가 출력되도록 한다.

IS_NUMERIC = "^[+]?\\d+(\\.\\d+)?$"

while True:
    inp2 = input("양의 실수를 입력하라")
    if not re.match(IS_NUMERIC, inp2):
        print("양의 실수를 입력해 주세요.")
    elif re.match(IS_NUMERIC, inp2): break
    
num2 = float(inp2)
num2 = math.sqrt(num2)
print(round(num2, 2))


# 29.3-3  제곱근 계산하기 - 개별 오류 메시지를 이용한 유효성 검사
# 데이터 입력의 유효성 검사를 위해 양수가 아닌 숫자값을 입력했을 때는 개별 오류 메시지를 출력해야 한다.

IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

while True:
    inp3 = input("양의 실수를 입력하라")

    failure = False

    if not re.match(IS_NUMERIC, inp3):
        failure = True
        print("숫자를 입력해 주세요.")

    elif re.match(IS_NUMERIC, inp3) and float(inp3) < 0: 
        failure = True
        print("양의 실수를 입력해 주세요.")
    
    if failure == False: break
    
num3 = float(inp3)
num3 = math.sqrt(num3)
print(round(num3, 2))


# 29.3-4  10개 숫자의 합 계산하기
# 10개의 숫자르 입력받고 이들 숫자의 합을 계산하고 출력하는 프로그램을 작성하라.

IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"
total = 0

for i in range(10):

    rand = input("양의 정수를 입력해 주세요")

    if not re.match(IS_NUMERIC, rand):
        print(rand, "숫자를 입력해 주세요.")

    elif float(rand) < 0: 
        print(rand, "음의 정수입니다.")
    
    else:
        total += float(rand)
    
    
print(total)