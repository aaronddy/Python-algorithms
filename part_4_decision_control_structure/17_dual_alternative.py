# 17.1-3  누가 가장 큰가?
# 두 수를 입력받아 변수 a와 b에 저장하고, 둘 중에 큰 값을 출력하는 순서도를 설계하고, 이에 대한 프로그램 작성하라

a = float(input("첫 번째 수를 입력하라"))
b = float(input("두 번째 수를 입력하라"))

# code 1_이중 택일
if a > b:

    max_num = a

else:

    max_num = b

print(max_num)


# code 2_단일 택일
maximum = a

if b > a:

    maximum = b

print(maximum)


# code 3_파이썬 메소드
maximum_num = max(a,b)

print(maximum_num)


# 17.1-4  홀수와 짝수 찾기
# 정수값을 입력받은 후, 입력값이 홀수 또는 짝수인지를 출력하는 순서도를 설계하고, 이에 대한 프로그램 작성하라

int_num = int(input("정수값을 입력하라"))

if int_num % 2 == 1:

    num = "홀수"

else:

    num = "짝수"

print("정수값은", num)



# 17.1-5  주급 계산하기
# 시간당 급여와 일주일 동안의 근로 시간을 입력받고, 일주일의 총 급여를 출력하는 순서도를 설계하고 프로그램 작성하라

pay_per_hour = float(input("시간당 급여는? "))
hours_for_week = float(input("일주일 동안의 근로 시간은? "))

if hours_for_week >= 40:

    under_40_hours = 40 * pay_per_hour
    over_40_hours = (hours_for_week - 40) * (pay_per_hour * 1.5)

    total_hours = under_40_hours + over_40_hours

else:

    total_hours = hours_for_week * pay_per_hour

print("일주일 총 급여는", total_hours)



