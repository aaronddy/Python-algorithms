# 다음과 같은 형태로 시간과 분을 출력하는 프로그램을 작성하라.

for i in range(24):
    for j in range(60):
        print(i, " ", j)


# 다음과 같은 결과를 출력하는 프로그램을 작성하라. 단 중첩 루프 제어 구조를 사용한다.

for i in range(5,0,-1):
    for j in range(i):
        print(i, end='')
    print()
    


# 다음과 같은 결과를 출력하는 프로그램을 작성하라. 단 중첩 루프 제어 구조를 사용한다.

for i in range(6):
    for j in range(i+1):
        print(j, end='')
    print()



# 다음과 같은 결과를 출력하는 프로그램을 작성하라. 단 중첩 루프 제어 구조를 사용한다.

for i in range(4):
    for j in range(10):
        print('*', end=' ')
    print()


# 다음과 같은 결과를 출력하는 프로그램을 작성하라. 단 중첩 루프 제어 구조를 사용한다.

n = int(input("몇각형을 원하는가?(3-20사이):"))

for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()


# 다음과 같은 결과를 출력하는 프로그램을 작성하라. 단 중첩 루프 제어 구조를 사용한다.

n2 = int(input("몇각형을 원하는가?(3-20사이):"))

for i in range(n2):
    for j in range(n2):
        if i == 0 or i == n2-1:
            print('*', end=' ')
        else:
            if j == 0 or j == n2-1:
                print("*", end=' ')
            else:
                print(' ', end=' ')
    print()


# 다음과 같은 결과를 출력하는 프로그램을 작성하라. 단 중첩 루프 제어 구조를 사용한다.

for i in range(6):
    for j in range(i):
        print('*', end=' ')
    print()

for i in range(4,0,-1):
    for j in range(i):
        print('*', end=' ')
    print()