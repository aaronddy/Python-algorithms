# 네 자릿수를 가진 정수 30개를 입력받은 후, 첫 번째 자릿수값이 5이고 마지막 자릿수값이 3인 정수들의 총합을 계산하고 출력하는 프로그램을 작성하라.

total = 0

for i in range(30):
    num = int(input("네 자릿수의 정수를 입력하라:"))
    digit1 = num // 1000
    digit4 = num % 10
    if digit1 == 5 and digit4 == 3:
        total += num

print(total)


# N개 정수를 입력받은 후, 짝수 정수의 총 개수를 출력하는 프로그램을 작성하라. N 값은 프로그램의 시작 부분에서 사용자로부터 입력받는다. 
# 모든 정수가 홀수라면, "짝수 정수를 입력하지 않았습니다."라는 메시지가 출력되도록 한다.

n = int(input("n 값을 입력하라:"))

count = 0
for i in range(n):
    num = int(input("정수를 입력하라:"))

    if num % 2 == 0:
        count += 1

if count <= 0:
    print("짝수 정수를 입력하지 않았습니다.")
else:
    print("result:", count)


# start와 finish라는 두 개의 정수를 이볅받은 후, start와 finish 사이에 5의 배수인 모든 정수를 출력하는 프로그램을 작성하라.
# 먼저 프로그램의 시작 부분에서 start 변수값이 finish 변수값보다 큰지를 검사해야 한다. 이런 경우가 발생하면 두 값을 서로 맞바꿔준다.

start = int(input("시작 정수를 입력하라:"))
finish = int(input("끝 정수를 입력하라:"))

# code1
if start > finish:
    for i in range(finish, start+1):
        if i % 5 == 0:
            print(i)

else:
    for i in range(start, finish+1):
        if i % 5 == 0:
            print(i)


# code2
if start > finish:
    C = start
    start = finish
    finish = C

for i in range(start, finish+1):
    if i % 5 == 0:
        print(i)


# 문자열 메시지를 입력받은 후, 이 메시지에 포함된 단어 수를 출력하는 프로그램을 작성하라.
# code1
msg = input("메시지를 입력하라.")
words = len(msg.split())

print("입력된 메시지는", words, "개의 단어를 포함하고 있습니다.")

# code2
msg2 = input("메시지를 입력하라.")
length = len(msg2)
count = 0

for i in range(length):
    if msg2[i] == " ":
        count += 1
    
    character = count + 1

print("입력된 메시지는", words, "개의 단어를 포함하고 있습니다.")



# 임의의 문자열을 입력받은 후, 단어별 평균 문제 개수를 출력하는 프로그램을 작성하라. 빈칸 문자는 세지 않는다.
msg3 = input("메시지를 입력하라.")
length2 = len(msg3)

count_space = 0

for j in range(length2):
    if msg3[j] == " ":
        count_space += 1
    
    characters = count_space + 1

avg_word = (length2 - count_space) / characters
print("단어별 평균 문자 개수는", round(avg_word, 2), "입니다.")   