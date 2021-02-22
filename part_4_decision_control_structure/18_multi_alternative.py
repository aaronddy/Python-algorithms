# -9999와 9999 사이의 정수값을 입력받고, 입력값에 대한 자릿수 개수를 출력하는 프로그램을 작성하라

num1 = int(input("-9999와 9999사이의 정수값을 입력하라"))

# code 1
if num1 <= 9 and num1 >= -9:

    print(num1, "한 자릿수 숫자입니다.")

elif num1 <= 99 and num1 >= -99:

    print(num1, "두 자릿수 숫자입니다.")

elif num1 <= 999 and num1 >= -999:

    print(num1, "세 자릿수 숫자입니다.")

else:

    print(num1, "네 자릿수 숫자입니다.")

# code 2

num1 = str(abs(num1))
print(len(num1), "자릿수 숫자입니다.")


# 월값을 숫자로 입력받고, 입력한 숫자값에 해당하는 계절을 출력하는 프로그램을 작성하라.

month = int(input("몇 월인가?"))

if month in [3,4,5]:

    season = 'spring'

elif month in [6,7,8]:

    season = 'summer'

elif month in [9,10,11]:

    season = 'actumn'

else:

    season = 'winter'

print('해당 계절은', season)


# A - F 까지의 값을 입력받고, 입력받은 학점에 대한 점수대를 출력하는 프로그램을 작성하라

grade = input("A-F 중 성적을 입력하라")

if grade == 'A': score = '99~100'
elif grade == 'B': score = '80~89'
elif grade == 'C': score = '70~79'
elif grade == 'D': score = '60~69'
else: score = '0~59'

print("grade:", grade, "score:", score)


# 다음 메뉴를 출력하고, 사용자로부터 메뉴의 선택값과 마일 수를 입력받은 후 사용자가 선택한 단위로 변환한 값을 출력하는 프로그램을 출력하라

print("1. 마일을 야드로 변환", "2. 마일을 피트로 변환", "3. 마일을 인치로 변환")

menu_num = int(input("몇 번 메뉴를 원하십니까?"))
mile = float(input("몇 마일입니까?"))

if menu_num == 1:

    trans = mile * 1760
    print("선택하신 메뉴는", menu_num, "변환 결과값은", trans, "yards.")

elif menu_num == 2:

    trans = mile * 5280
    print("선택하신 메뉴는", menu_num, "변환 결과값은", trans, "feet.")

elif menu_num == 3:

    trans = mile * 63360
    print("선택하신 메뉴는", menu_num, "변환 결과값은", trans, "inches.")

else:

    print("잘못 입력하셨습니다")
