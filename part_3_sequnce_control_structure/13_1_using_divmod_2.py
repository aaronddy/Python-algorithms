# 13.1-3  경과시간 출력하기
# 초 단위의 경과 시간을 정수로 입력받고, "DD일 HH시간 MM분 SS초" 형식으로 출력하는 파이썬 프로그램 작성하기

number = int(input("초 단위의 경과 시간을 입력하여라. "))

if number >= 86400:

    days, r = divmod(number, 86400)
    hours, r = divmod(r, 3600)
    minutes, seconds = divmod(r, 60)

    print("기준 시점으로부터 경과 시간은", days, "일", hours, "시간", minutes, "분", seconds, "초 입니다.")

elif number < 86400 and number >= 3600:

    hours, r = divmod(number, 3600)
    minutes, seconds = divmod(r, 60)

    print("기준 시점으로부터 경과 시간은", hours, "시간", minutes, "분", seconds, "초 입니다.")

else:

    minutes, seconds = divmod(number, 60)

    print("기준 시점으로부터 경과 시간은", minutes, "분", seconds, "초 입니다.")




# 13.1-4  숫자를 역순으로 바꾸기
# 세 자릿수의 정수를 입력받고, 그 정수를 역순으로 바꾸어 주는 파이썬 프로그램 작성하기

nums = int(input('세 자릿수의 정수를 입력하라. '))

digit1, r = divmod(nums, 100)
digit2, digit3 = divmod(r, 10)

reverse_nums = digit3 * 100 + digit2 * 10 + digit1

print("입력받은 정수의 역수는 ", reverse_nums)