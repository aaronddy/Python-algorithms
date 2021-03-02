# 순차 제어 구조로 표현한다면?

total = 0

a = float(input())
total = total + a

a = float(input())
total = total + a

a = float(input())
total = total + a

a = float(input())
total = total + a


# 순차 제어 구조를 루프 제어 구조로
'''
execute_these_statements_4_times:

    a = float(input())
    total = total + a

print(total)

'''

# while loop을 사용한다면?

while total < 100:
    a = float(input())
    total = total + a

print(total)