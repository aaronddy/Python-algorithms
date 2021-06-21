# 33.4 1차원 리스트를 2차원 리스트와 함께 사용하기

# 33.4-1 평균값 찾기
# 다섯 개 과목에 대한 성적을 받은 열 명의 학생이 있다고 가정할 때, 모든 과목에 대해 학생 이름과 성적을 입력받아 학생별 평균 점수를 계산하고 한 개 이상의 과목 성적이 89점보다 높은 학생의 이름을 출력하는 프로그램을 작성하라.
import random

# 학생명 - 1차원 / 5개 과목 성적 - 2차원 리스트 생성

STUDENTS = 10
LESSONS = 5

# 학생 이름과 성적 리스트 생성
students = [None] * STUDENTS
grades = [ [None] * LESSONS for i in range(STUDENTS)]

# 학생 이름과 성적 리스트에 값 넣기
for i in range(STUDENTS):
    students[i] = input("학생의 이름을 입력하세요:")

    for j in range(LESSONS):
        grades[i][j] = random.randint(0, 100)

print("studnets_lst:", students)
print("grades_lst:", grades)


# count 리스트 생성 및 값 넣기
mean_grades = [None] * STUDENTS
counter = [None] * STUDENTS

for i in range(STUDENTS):
    mean_grades[i] = 0
    counter[i] = 0

    for j in range(5):
        mean_grades[i] += grades[i][j]
        
        if grades[i][j] > 89:
            counter[i] += 1

    mean_grades[i] /= 5

print("mean_grades:", mean_grades)
print("counter:", counter)


# 89점보다 높은 학생이름 출력하기
for i in range(STUDENTS):
    if counter[i] >= 1:
        print(students[i])