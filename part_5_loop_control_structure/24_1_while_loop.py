# 불리언 식의 결과가 True이면 명령문 블록이 수행되고, 결과가 False이면 루프를 벗어난다.

# code1
# 아래의 while loop은 작동하지 않는다.

total = 0

while total >= 100:
    a = float(input("code1:"))
    total = total + a

print(total)

'그 이유는 불리언 식의 결과가 항상 False이기 때문이다. total = 0으로 초기 설정이 되어 있기 때문에 애초에 total >= 100이 성립할 수가 없다. 따라서 항상 False이고 while loop에 해당하는 명령문 블록이 수행되지 않고 0을 출력한다.'

# code2
# 아래의 while loop은 작동한다.

while total <= 100:
    a = float(input("code2:"))
    total = total + a

print(total)

'해당 루프는 total = 0으로 초기설정 되었기에 불리언 식의 결과가 total > 0 전까지는 True이다. 따라서 조건이 만족할 때까지는 명령문 블록이 수행된다.'


# 24.1-5  네 개 숫자의 총합 구하기
# 네 개의 숫자를 입력받고, 이들 숫자의 총합을 출력하는 프로그램을 작성하라

num_sum = 0
i = 4

while i > 0:
    num = float(input("네 개의 숫자:"))
    num_sum += num
    i -= 1
    print(i, num_sum)

print("total:", num_sum)


# 24.1-6  숫자 20개의 곱 구하기

num_multiply = 1
i = 20

while i > 0:
    nums = float(input("20개의 숫자:"))
    num_multiply *= nums
    i -= 1

print("total:", num_multiply)


# 24.1-7  숫자 N개의 곱 구하기

n = int(input("양의 정수를 입력해 주세요:"))
p = 1

while n > 0:
    n_num = float(input("n개의 숫자:"))
    p *= n_num
    n -= 1

print("total: ", p)


# 24.1-8  홀수의 합 구하기
# 20개의 정수를 입력받고, 이들 정수 중 홀수의 합을 계산하고 출력하는 프로그램을 작성하라.

sum_odd = 0
j = 20

while j > 0:

    odds = int(input('정수를 입력하라:'))

    if odds % 2 == 1:
        sum_odd += odds
    j -= 1

print(sum_odd)


# 24.1-9  정해져 있지 않은 개수의 숫자 합 계산하기
# -1 값을 입력할 때까지 반복해 숫자값을 읽어 들이는 프로그램을 작성하라. 입력이 완료되면 입력 숫자의 총합을 화면에 출력한다(-1 값은 총합에 포함하지 않는다.)

sum_undefined = 0
value = 0

while value != -1:
    
    sum_undefined += value
    value = float(input())

print(sum_undefined)