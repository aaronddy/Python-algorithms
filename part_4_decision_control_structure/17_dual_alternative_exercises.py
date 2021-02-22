# 정수값을 입력받고, 입력값이 6의 배수인지 여부를 출력하는 프로그램을 작성하라

num1 = int(input("정수값을 입력하라"))

if num1 % 6 == 0:

    print("입력받은 정수값은 6의 배수이다")

else:

    print("6의 배수가 아니다")


# 정수값을 입력받고, 입력값이 6 또는 7의 배수인 경우와 그렇지 않은 경우(6 또는 7의 배수가 아닌 경우)에 서로 다른 메시지를 출력하는 프로그램을 작성하라

if (num1 % 6 == 0) or (num1 % 7 == 0):

    print(num1, "6 또는 7의 배수이다")

else:

    print(num1, "6 또는 7의 배수가 아니다")


# 정수값을 입력받고, 입력값이 4의 배수인지 여부를 출력하는 프로그램을 작성하라. 단 입력값을 4로 나누었을 때 몫과 나머지를 출력해야 한다.

value = num1 // 4
remain = num1 % 4

if remain == 0:

    print(num1, "4의 배수이다")

else:

    print(num1, "4의 배수가 아니다")

print('"', num1, '= 4 *', value, '+', remain)


# 정수값을 입력받고, 입력값이 네 자리 정수인지 여부를 출력하는 프로그램을 작성하라.

num2 = int(input("정수값을 입력하여라"))

value = num2 / 1000

if value >=1 and value < 10:

    print(num2, "네 자리 정수이다")

else:

    print(num2, "네 자리 정수가 아니다")


# 두 개의 정수값을 입력받고, 입력값 중 작은 값을 출력하는 프로그램을 작성하라

min_num = min(num1, num2)
print("작은 값은", min_num)


# 세 개의 정수값을 입력받고, 입력값을 길이로 하여 삼각형을 만들 수 있는지의 여부를 출력하라

tri_num1 = int(input("첫 번쩨 정수값을 입력하라"))
tri_num2 = int(input("두 번쩨 정수값을 입력하라"))
tri_num3 = int(input("세 번쩨 정수값을 입력하라"))

if tri_num1 < tri_num2+tri_num3 and tri_num2 < tri_num1+tri_num3 and tri_num3 < tri_num1+tri_num2:

    print("입력값으로 삼각형을 만들 수 있다")

else:

    print("입력값으로 삼각형을 만들 수 없다.")


# 세 개의 멀리뛰기 거기 값을 입력받고, 세 값의 평균 거리가 8미터 이상이면 "통과", 미만이면 "실패"를 출력하는 프로그램을 작성하라

jump_num1 = float(input("첫 번쩨 값을 입력하라"))
jump_num2 = float(input("두 번쩨 값을 입력하라"))
jump_num3 = float(input("세 번쩨 값을 입력하라"))

if (jump_num1+jump_num2+jump_num3) / 3 >= 8:

    print("pass")

else:

    print("fail")


# 운행한 마일 수를 입력받고, 다음 정기 점검 서비스를 받을 때까지 남은 운행 마일 수와 서비스 종류를 출력하는 프로그램을 작성하라.

miles = float(input("운행한 마일 수는 몇인가?"))

# 단기 정기 점검 서비스

if 6000 - miles >= 0:

    left_days = 6000 - miles

else:

    left_days = miles - 6000
    
print(left_days, "단기 정기 점검 서비스")

# 장기 정기 점검 서비스

if 12000 - miles >= 0:

    left_days = 12000 - miles

else:

    left_days = miles - 12000

print(left_days, "장기 정기 점검 서비스")