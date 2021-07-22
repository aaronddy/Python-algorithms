# 35.2-1 홀수를 역순으로 출력하기 - 오류 메시지 없이 확인하기
import random

SIZE = 20
lst_odds = []

for i in range(SIZE):
    while True:
        input_data = random.randint(0, 50)
        print("input", input_data)
        if input_data % 2 == 1: break
        
    lst_odds.append(input_data) 
    print("lst_in_process:", lst_odds)    
           
print("lst_odds:", lst_odds)

# 역순으로 출력
for i in lst_odds[::-1]:
    print(i, end='\t')


# 35.2-2 홀수를 역순으로 출력하기 - 하나의 오류 메시지로 확인하기
# 기억하기: while loop은 애초에 조건이 맞아야 loop이 돌아간다.

lst_odds2 = [None] * SIZE

for i in range(20):

    input_data = random.randint(0, 50)
    print("first_input:", input_data)
    while input_data % 2 == 0:     
        print("홀수가 아닙니다.")    
        input_data = random.randint(0, 50)
        if input_data % 2 == 1: break

    print("odd_input:", input_data)        
    lst_odds2[i] = input_data

    print("lst2_in_progress:", lst_odds2)

# 역순으로 출력
for i in lst_odds2[::-1]:
    print(i, end='\t')


# 35.2-3 홀수를 역순으로 출력하기 - 개별 오류 메시지로 확인하기

print("======================================")
lst_odds3 = []

for i in range(SIZE):
    
    input_data = random.randint(-50, 50)
    while True:
        failure = False

        if input_data < 0:
            print("음수입니다.")
            input_data = random.randint(0, 50)
            failure = True
        
        elif input_data == 0:
            print("0입니다.")
            input_data = random.randint(1, 50)
            failure = True

        elif input_data % 2 == 0:
            print("양의 짝수입니다.")
            input_data = random.randint(1, 50)
            failure = True
        
        if failure == False: break

    lst_odds3.append(input_data)
    print("lst_odds3:", lst_odds3)