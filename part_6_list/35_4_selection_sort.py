# 35.4-9  두 번째 리스트와 관계를 유지하면서 1차원 리스트 정렬하기
# 일 년 동안 매월달에 전력 사용량을 입력받아 월별 전력 사용량과 해당 월을 내림차순으로 출력하는 프로그램을 작성하라. 선택 정렬 알고리즘을 사용하라.

import random

months = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
SIZE = len(months)

kwh = [None] * SIZE
for i in range(SIZE):
    kwh[i] = random.randint(100, 500)

print("kwh:", kwh)

for m in range(SIZE):
    min_kwh = kwh[m]
    index_min = m
   
    for i in range(m, SIZE):
        if kwh[i] < min_kwh:
            min_kwh = kwh[i]
            index_min = i
            print("min_kwh:", min_kwh)
            print("index:", index_min)
           

    kwh[m], kwh[index_min] = min_kwh, kwh[m]
    months[m], months[index_min] = months[index_min], months[m]
    print("sorting_kwh:", kwh)
    print("sorting_months:", months)
