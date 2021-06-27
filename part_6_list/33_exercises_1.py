import random
import math

# 1.

STUDENTS = ['Jamie', 'Oliver', 'May', 'Olivia', 'Sam']
SUBJECTS = ['Math', 'Spanish', 'Science', 'History']
grades = [ [None] * len(SUBJECTS) for i in range(len(STUDENTS)) ]
grades_mean = [ [None] for i in range(len(STUDENTS)) ]

for i in range(len(STUDENTS)):
    grades_mean[i] = 0
    total = 0

    for j in range(len(SUBJECTS)):

        grades[i][j] = random.randint(40, 100)
        total += grades[i][j]

    grades_mean[i] = total / len(SUBJECTS)

print("grades:", grades)
print("mean:", grades_mean)


for i in range(len(STUDENTS)):

    score = ''

    if grades_mean[i] >= 90 and grades_mean[i] <= 100:
        score = 'A'
    elif grades_mean[i] >= 80 and grades_mean[i] <= 89:
        score = 'B'
    elif grades_mean[i] >= 70 and grades_mean[i] <= 79:
        score = 'C'
    elif grades_mean[i] >= 60 and grades_mean[i] <= 69:
        score = 'D'
    elif grades_mean[i] >= 0 and grades_mean[i] <= 59:
        score = 'E'

    print(STUDENTS[i], "의 학점은", score)



print('==========')


# 3.
PLAYERS = 15
GAMES = 12

back_num = [ [None] for i in range(PLAYERS)]
scores = [ [None] * GAMES for i in range(PLAYERS)]

for i in range(PLAYERS):    
    back_num[i] = random.randint(1, 100)

    for j in range(GAMES):
        scores[i][j] = random.randint(0, 35)

print("back_num:", back_num)
print("score:", scores)

# 선수별 총득점
score_players = [ [None] for i in range(PLAYERS)]

for i in range(PLAYERS):
    score_players[i] = 0

    for j in range(GAMES):
        score_players[i] += scores[i][j]

    print(back_num[i], "선수의 총득점:", score_players[i])

print("선수별 총득점:", score_players)

# 경기별 총득점
score_games = [ [None] for i in range(GAMES)]

for j in range(GAMES):
    score_games[j] = 0

    for i in range(PLAYERS):
        score_games[j] += scores[i][j]

    print(j+1, "번째 경기의 총득점:", score_games[j])

print("경기별 총득점:", score_games) 


print('========')

# 8.
MONTHS = 12
PERSONS = 10

weights = [ [None] * MONTHS for i in range(PERSONS) ]
heights = [ [None] * MONTHS for i in range(PERSONS) ]

w_mean = [[None] for i in range(PERSONS) ]
h_mean = [[None] for i in range(PERSONS) ]
BMI = [[None] for i in range(PERSONS) ]

for i in range(PERSONS):
    w_mean[i] = 0
    h_mean[i] = 0
    BMI[i] = 0

    for j in range(MONTHS):

        weights[i][j] = random.randint(45, 100)
        heights[i][j] = random.randint(145, 195)

        w_mean[i] += weights[i][j]
        h_mean[i] += heights[i][j]
        BMI[i] += weights[i][j] / ((heights[i][j] * 0.01) ** 2)

    w_mean[i] /= MONTHS
    h_mean[i] /= MONTHS
    BMI[i] /= MONTHS

    w_mean[i] = round(w_mean[i], 1)
    h_mean[i] = round(h_mean[i], 1)
    BMI[i] = round(BMI[i], 1)

print("w_mean:", w_mean)
print("h_mean:", h_mean)
print("BMI_mean:", BMI)

for i in range(PERSONS):
    
    BMI_5 = weights[i][4] / ((heights[i][4] * 0.01) ** 2)
    BMI_7 = weights[i][7] / ((heights[i][7] * 0.01) ** 2)

    print("order", i+1)
    print("5_BMI:", round(BMI_5, 1))
    print("8_BMI:", round(BMI_7, 1))
    print("==")