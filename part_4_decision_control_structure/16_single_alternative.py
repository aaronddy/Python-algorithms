# 16.1-2  숫자의 절대값 구하기

num = float(input("숫자를 입력하여라"))

if num < 0:

    num = abs(num)

print(num)



# 하나의 숫자를 입력받고, 그 값이 양수인 경우 "양수"를 출력하라

num1 = float(input("숫자를 입력하라"))

if num1 > 0:

    print("양수")


# 두 개 값을 입력받고, 두 입력값 모두 양수일 경우 "양수"를 출력하라

num2 = float(input("숫자를 입력하라"))
num3 = float(input("숫자를 입력하라"))

if num2 > 0 and num3 >0:

    print("양수")



# 한 개 값을 입력받고, 그 값이 숫자인 경우 "숫자"를 출력하라

import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

value = input("값을 입력하여라")

if re.match(IS_NUMERIC, value):

    print("숫자")


# 문자열을 입력받고, 입력받은 문자열이 모두 대문자인 경우 "대문자"를 출력하라

cha = input("영문자열을 입력하라")

if cha == cha.upper():

    print("대문자")


# 문자열을 입력받고, 입력받은 문자열의 길이가 20자 이상인 경우 "장문"을 출력하라

if len(cha) >= 20:
    
    print("장문")


# 네 개의 숫자값을 입력받고, 입력값 중 하나라도 음수가 있는 경우 "음수"를 출력하라

num4 = float(input("숫자를 입력하라"))

if num1 < 0 or num2 < 0 or num3 < 0 or num4 < 0:

    print("음수")


# 두 개의 숫자값을 입력받고, 첫 번째 숫자가 두 번째 숫자보다 크면 두 변수의 값을 맞바꾸어 입력받은 두 수를 항상 오르차순으로 출력하라

if num1 > num2:

    change = num1
    num1 = num2
    num2 = change

    print(num1, num2)


# 세 지역의 온도값을 입력받고, 세 지역의 평균 온도가 35도 이상인 경우 "폭염경보"를 출력하라

temp1 = float(input("서울의 온도는?"))
temp2 = float(input("용인의 온도는?"))
temp3 = float(input("광주의 온도는?"))

average_temp = (temp1+temp2+temp3) / 3 

if average_temp >= 35:
    
    print("폭염경보")