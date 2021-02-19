# 연습문제

# 1. 입력받은 임의의 정수의 마지막 자릿수값에 8을 곱한 후, 그 결과 출력하라

num1 = int(input("정수를 입력하라"))

r, digit1 = divmod(num1, 10)
result1 = digit1 * 8

print("결과값은 ", result1)


# 2. 결정 제어 구조를 사용하지 않고 입력받은 정수값이 홀수이면 1, 그렇지 않으면 0을 출력하라

num2 = int(input("정수를 입력하라"))

result2 = num2 % 2
print(result2)


# 3. 인출 금액을 입력받아 ATM이 지급할 수 있는 각 지급액 단위별 최소 금액을 출력하는 파이썬 프로그램을 작성하라

num3 = int(input("인출 금액을 입력하라"))

if num3 >= 50000:

    unit1, r = divmod(num3, 50000)
    unit2, unit3 = divmod(r, 10000)

    if unit2 >= 1 and unit3 >=1:

        print("오만 원", unit1, "장,", "만 원", unit2, "장,", "천 원", unit3, "장")
    
    elif unit2 == 0 and unit3 >= 1:

        print("오만 원", unit1, "장,", "천 원", unit3, "장")
    
    elif unit2 >= 0 and unit3 == 0:

        print("오만 원", unit1, "장,", "만 원", unit2, "장,")

    else:

        print("오만 원", unit1, "장")

elif num3 < 50000 and num3 >= 10000:

    unit2, unit3 = divmod(num3, 10000)

    if unit3 >= 1:

        print("만 원", unit2, "장,", "천 원", unit3, "장")

    else:

        print("만 원", unit2, "장")

else:

    unit3 = num3 // 1000
    
    print("천 원", unit3, "장")
