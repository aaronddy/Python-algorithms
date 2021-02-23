# 삼각형의 세 변의 길이를 입력받고, 입력값으로 삼각형을 만들 수 있는지의 여부를 출력하는 프로그램을 작성하라
# 삼각형을 만들 수 없다면 이에 대한 메시지를 출력하고, 삼각형을 만들 수 있다면 다음 삼각형이 가능한지 판단하여라.
# a. 정삼각형  b. 직각삼각형  c. 이외의 삼각형

line_1 = float(input("첫 번째 변의 길이를 입력하라")) 
line_2 = float(input("두 번째 변의 길이를 입력하라"))
line_3 = float(input("세 번째 변의 길이를 입력하라"))

if not(line_1 < line_2+line_3 and line_2 < line_1+line_3 and line_3 < line_1+line_2):

    print("삼각형을 만들 수 없습니다.")

else:

    if line_1 == line_2 and line_2 == line_3:

        print('정삼각형을 만들 수 있습니다.')

    elif (line_1 ** 2 == line_2 ** 2 + line_3 ** 2) or (line_2 ** 2 == line_1 ** 2 + line_3 ** 2) or (line_3 ** 2 == line_2 ** 2 + line_1 ** 2):

        print('직각삼각형을 만들 수 있습니다.') 

    else:

        print('삼각형을 만들 수 있습니다.')



# 온도와 풍속에 대한 값을 입력받고, 온도값이 30도 이상이면 "뜨겁고"를 출력, 30도 미만이면 "차갑고"를 출력하며, 풍속이 8m/s 이상이면 "바람이 강하다" 출력, 8m/s 미만이면 "바람이 약하다"를 출력하는 프로그램을 작성.
# 출력 메시지는 한 문장이어야 한다.

# code1
temp = float(input("온도를 입력하세요(도)"))
wind = float(input("풍속을 입력하세요(m/s)"))

if temp >= 30:
    if wind >= 8:
        print("오늘은 뜨겁고 바람이 강합니다.")

    else:
        print("오늘은 뜨겁고 바람이 약합니다.")

else:
    if wind >= 8:
        print("오늘은 차갑고 바람이 강합니다.")
    
    else:
        print("오늘은 차갑고 바람이 약합니다.")

# code2

if temp >= 30:
    m1 = "뜨겁고"

else:
    m1 = "차갑고"

if wind >= 8:
    m2 = "강합니다."

else:
    m2 = "약합니다."

print("오늘은", m1, "바람이", m2)



# 초기에 사용자로부터 네 자리 비밀번호를 입력받는다(비밀번호는 "1234"라고 가정). 비밀번호가 올바르면 사용자로부터 출금액을 입력받는다.
# 출금액을 입력받은 후 해당 금액을 가장 적은 수의 지폐로 출금해야 하며, 각 지폐권의 개수를 입력한다. 
# 잘못된 비밀번호 입력에 대한 허용 횟수는 2회로 하며, 비밀번호 입력이 3회 연속 잘못되었다면 "계정 잠금"이라는 메시지 출력 후 프로그램을 종료한다. 

pwd = input("네 자리 비밀번호를 입력하라")

if pwd != "1234":
    
    pwd = input("틀린 비밀번호, 다시 네 자리 비밀번호를 입력하라")
    
    if pwd != "1234":

        pwd = input('틀린 비밀번호, 다시 네 자리 비밀번호를 입력하라')

    
        
if pwd != "1234":

    print("계정 잠금")

else:

    drawler = int(input('출금 금액을 입력하라'))

    unit1, r = divmod(drawler, 50000)
    unit2, r = divmod(r, 10000)
    unit3, unit4 = divmod(r, 5000)

    print("5만 원권", unit1, "장, 1만 원권", unit2, "장, 5천 원권", unit3, "장, 천 원권", unit4, "장 출금")


'''
    if drawler >= 50000:

        unit1, r = divmod(drawler, 50000)
        unit2, r = divmod(r, 10000)
        unit3, unit4 = divmod(r, 5000)

        print("5만 원권", unit1, "장, 1만 원권", unit2, "장, 5천 원권", unit3, "장, 천 원권", unit4, "장 출금")

    elif drawler < 50000 and drawler >= 10000:

        unit2, r = divmod(drawler, 10000)
        unit3, unit4 = divmod(r, 5000)

        print("1만 원권", unit2, "장, 5천 원권", unit3, "장, 천 원권", unit4, "장 출금")

    elif drawler < 10000 and drawler >= 5000:

        unit3, unit4 = divmod(drawler, 5000)

        print("5천 원권", unit3, "장, 천 원권", unit4, "장 출금")

    else:

        unit4 = drawler

        print("천 원권", unit4, "장 출금")

'''