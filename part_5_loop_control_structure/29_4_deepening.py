# 29.5  루프 제어 구조를 이용하여 최솟값과 최댓값 찾기

# 단일-택일 결정 구조를 이용하여 네 개의 값 중에서 최댓값을 찾아보자.
w = int(input("값을 입력하라"))          # 첫 번째 값을 입력
maximum = w

w = int(input("값을 입력하라"))          # 두 번째 값을 입력
if w > maximum:
    maximum = w

w = int(input("값을 입력하라"))          # 세 번째 값을 입력
if w > maximum:
    maximum = w

w = int(input("값을 입력하라"))          # 네 번째 값을 입력
if w > maximum:
    maximum = w

print("최대값은", maximum)


# 위의 코드를 for loop으로 전환하기

for i in range(3):                   # 두 번째, 세 번째, 네 번째 값을 입력
    w = int(input("값을 입력하라"))
    if w > maximum:
        maximum = w

print("최대값은", maximum)



# 29_5b  10명의 사랍 중에서 몸무게가 가장 많이 나가는 사람을 찾고 그 결과를 출력하는 프로그램을 작성하라.
maximum = -1

for i in range(10):
    w = int(input("몸무게를 입력하라"))
    if w > maximum:
        maximum = w
        print(maximum)

print("maximum weight is", maximum)


# 29.5-1  최솟값과 최댓값 검증하고 찾기
# 10명의 몸무게를 입력받고 몸무게가 가장 적게 나가는 사람을 찾아 주는 프로그램을 작성하라. 또한, 사용자가 숫자가 아닌 값, 음숫값, 0 값, 또는 680 이상의 값을 입력했을 때 오류 메시지가 출력되도록 한다.
import re

# regex는 string 타입에만 적용 가능
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"
max_w = -1

for i in range(10):
    weight = input("몸무게를 입력하세요.")
    if not re.match(IS_NUMERIC, weight) or float(weight) <= 0 or float(weight) >= 680:
        print("몸무게를 제대로 입력하세요.")
    elif re.match(IS_NUMERIC, weight) and float(weight) > max_w:
        max_w = float(weight)

print("maximum weight is", max_w)


# 29.5-2  최대 온도를 검증하고 찾기
# "STOP" 단어를 입력할 때까지 행성 이름과 행성의 평균 온도를 연속해서 입력받는 프로그램을 작성하라. 그리고 가장 높은 온도를 가진 행성의 이름을 출력한다.

m_name = ''
max_temp = -273.15
default_temp = -273.15

name = input("행성 이름을 입력하세요.")
while name.upper() != "STOP":
    
    avg_temp = input("행성의 평균 온도를 입력하세요.")

    while not re.match(IS_NUMERIC, avg_temp) or float(avg_temp) < default_temp:
        print("잘못된 값입니다.")
        avg_temp = input("행성 평균 온도를 다시 입력하세요. 절대 영도 -273.15보다는 커야 합니다.")
    
    print(name, avg_temp)
    
    if float(avg_temp) > max_temp:
        max_temp = float(avg_temp)  
        m_name = name                                # 최대 온도값의 행성 이름을 m_name에 저장함으로써 name과 구분
        print(m_name, max_temp)

    name = input("행성 이름을 입력하세요.")                # 행성 이름 초기화


print("최대 온도 행성은", m_name)


# 29.5-3  학점 매기기
# 20명의 학생이 있다. 학생들의 수학 점수(0-100)를 입력하고 가장 높은 점수의 학생과 A학점(90-100)을 받은 학생 수를 출력하는 프로그램을 작성하라. 
# 데이터 유효성을 검사해야 하며, 0부터 100 까지의 값만을 입력받아야 한다.

count_a = 0
highest = 0

for i in range(20):
    score = input('점수를 입력하세요')

    while not re.match(IS_NUMERIC, score) or float(score) < 0 or float(score) > 100:
        print("잘못된 점수입니다. 0-100 사이의 점수를 입력하세요.")
        score = input('점수를 입력하세요')

    print("학생 번호", i+1, "입력 점수:", score)
    
    if 90 <= float(score) <= 100:
        count_a += 1
    
    print("A학점 인원:",count_a)

    if float(score) > highest:
        highest = float(score)

print("가장 높은 점수:", highest, "총 A학점 인원:", count_a)