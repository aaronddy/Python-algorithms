# 35.4-6  변형된 버블 정렬 알고리즘 - 1차원 리스트 정렬하기
# 20명의 몸무게를 입력받아 가장 무거운 3명과 가장 가벼운 3명의 몸무게를 출력하는 프로그램을 작성하라. 단, 변형된 버블 정렬 알고리즘을 사용하여라.

import random

W_SIZE = 20
weights = [None] * W_SIZE

for i in range(W_SIZE):
    weights[i] = random.randint(45, 100)

print("weights:", weights)

for w in range(W_SIZE-1):
    # flag 추가
    swaps = False
    for i in range(W_SIZE-1, w, -1):
        if weights[i] < weights[i-1]:
            weights[i], weights[i-1] = weights[i-1], weights[i]
            swaps = True
    
    # 한번도 자리변경이 없었으면, loop 종료
    if swaps == False: break

print("가장 가벼운 3명의 몸무게:", weights[0], weights[1], weights[2])
print("가장 무거운 3명의 몸무게:", weights[W_SIZE-1], weights[W_SIZE-2], weights[W_SIZE-3])



# 35.4-7  세명의 최고 득점자

T_SIZE = 3
P_SIZE = 10
team = ['FC Barcelona', 'Real Madrid CF', 'Sevilla FC']
player = [['Sergino Dest', 'Gerad Pique', 'Ronald Araujo', 'Sergio Busquets', 'Antoine Griezmann', 'Miralem Pjanic', 'Martin Braithwaite', 'Lionel Messi', 'Ousmane Dembeie', 'Riqui Puig'], ['Daniel Carbajal', 'Eder Militao', 'David Alaba', 'Raphael Varane', 'Nacho Fernandez', 'Eden Hazard', 'Toni Kroos', 'Karim Benzema', 'Luca Modric', 'Marco Asensio'], ['Joris Gnagnon', 'Sergi Gomez', 'Karim Rekik', 'Lucas Ocampos', 'Nemanja Gudelj', 'Suso Fernandez', 'Joan Jordan', 'Luuk de Jong', 'Ivan Rakitic', 'Munir El Hadaddi']]
grades = [[None] * P_SIZE for i in range(T_SIZE)]

for i in range(T_SIZE):
    for j in range(P_SIZE):
        grades[i][j] = random.randint(0, 30)

print("grades:", grades)

for i in range(T_SIZE):
    w = 0
    flags = False 
    while w < P_SIZE-1:
        for j in range(P_SIZE-1, w, -1):
            if grades[i][j] < grades[i][j-1]:
                grades[i][j], grades[i][j-1] = grades[i][j-1], grades[i][j]
                player[i][j], player[i][j-1] = player[i][j-1], player[i][j]
                flags = True
                print("bubbling_grades:", grades)
        w += 1
        if flags == False: break

print("grades_after:", grades)
print("FC Barcelona 1st", player[0][P_SIZE-1], grades[0][P_SIZE-1])
print("FC Barcelona 2nd", player[0][P_SIZE-2], grades[0][P_SIZE-2])
print("FC Barcelona 3rd", player[0][P_SIZE-3], grades[0][P_SIZE-3])

print("Real Madrid CF 1st", player[1][P_SIZE-1], grades[1][P_SIZE-1])
print("Real Madrid CF 2nd", player[1][P_SIZE-2], grades[1][P_SIZE-2])
print("Real Madrid CF 3rd", player[1][P_SIZE-3], grades[1][P_SIZE-3])

print("Sevilla FC 1st", player[2][P_SIZE-1], grades[2][P_SIZE-1])
print("Sevilla FC 2nd", player[2][P_SIZE-2], grades[2][P_SIZE-2])
print("Sevilla FC 3rd", player[2][P_SIZE-3], grades[2][P_SIZE-3])