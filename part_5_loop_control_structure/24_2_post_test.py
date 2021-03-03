'''
파이썬 프로그램에서 사후-검사 루프 구조를 지원하고 있지 않으나, 사용할 수는 있다. 간접 방식으로 if와 break 명령문을 이용한다.
해결 방법은 무한 루프를 우선 만들고 명령문 블록 다음에 불리언 식을 두는 것이며, 이 불리언 식이 True로 평가되면 루프를 벗어나게 하는 것이다.

while True:
    명령문 블록
    if 불리언 식: break

'''

# 1부터 10까지의 숫자를 출력

i = 1
while True:
    print(i)
    i += 1
    if i > 10: break


# 24.2-2  총 반복 횟수 세기
# 다음 프로그램에서 수행되는 총 반복 횟수는?

i = 3
while True:
    i -= 1
    if i < 0: break

print("End")   # 4 times


# 24.2-3 사후-검사 루프 구조를 사전-검사 루프 구조로 변경하기
print('사후-검사 루프')
i = -1
while True:
    i -= 1
    print('안녕하세요')
    if i <= 0: break

print("끝!")
print('================')

print('사전-검사 루프')
i = -1
while i > 0:
    i -= 1
    print('안녕하세요')

print("끝!")


# 24.2-5  숫자 N개의 곱 계산하기
# N개의 숫자를 입력받고, 이들 숫자의 곱을 계산하고 출력하는 프로그램을 작성하라.

print('사후-검사 루프')
n = int(input("n을 입력하라:"))
multiple = 1

while True:
    num = float(input('숫자를 입력하라:'))
    multiple *= num
    n -= 1
    if n <= 0: break

print("결과값은:", multiple)
print("================")
print("사전-검사 루프")

n2 = int(input("n을 입력하라:"))
multiple2 = 1
while n2 > 0:
    num2 = float(input('숫자를 입력하라:'))
    multiple2 *= num2
    n2 -= 1

print("결과값은:", multiple2)


# 24.2-6  정해져 있지 않은 개수의 숫자 곱 계산하기
# -1 값을 입력할 때까지 반복하여 숫자값을 읽는 프로그램을 작성하라. 입력이 완료되면, 입력 숫자의 곱을 화면에 출력한다(-1 값은 최종 곱 결과에 포함하지 않는다).

multiple3 = 1
num3 = float(input('숫자를 입력하라'))

while True:
    if num3 == -1: break

    multiple3 *= num3
    num3 = float(input('숫자를 입력하라'))

print('결과값은:', multiple3)