# 19.1-2  양수, 음수, 0 판단하기
# 숫자값을 입력받고, 입력값이 양수인지 음수인지 아니면 0인지를 출력하는 프로그램을 작성하라

num1 = float(input("숫자를 입력하라"))

if num1 >= 0:
    if num1 == 0:
        print("0")

    else:
        print("양수")

else:
    print("음수")

    