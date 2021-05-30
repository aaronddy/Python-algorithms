# 31.4 1차원 리스트에 반복문 적용하기
# 1차원 리스트에 반복 처리를 적용하는 데에는 크게 두 가지 방법이 있다.

'''
1. 인덱스를 사용하여 리스트의 각 요소를 참조하는 방식이며, 이에 대한 일반 형태는 다음과 같다.

for index in range(size):
    process list_name[index]

'''

weather = ["clody", "rain", "sunny", "snow"]

for idx in range(4):
    # temp = float(input("오늘의 온도는?"))
    print(weather[idx])



'''
2. 리스트 전체를 참조하는 방식이다.

for i in list_name:
    process i

'''

for i in weather:
    print("today's weatehr:", i)



# 31.4-1 역순으로 단어 출력하기

for i in range(4):
    print("first", weather[-(i+1)]) 

for i in range(3, -1, -3):
    print("second", weather[i])

for i in weather[::-1]:
    print("third", i)


# 31.4-2 역순으로 양수 출력하기
int_list = [3, 8, -3, -10, 33, 22, 0, 3, 2, 11, -20]

count = 0
for i in int_list[::-1]:
    if i > 0:
        count += 1
        print("양수 개수", count, "양수:",i)


# 31.4-3 인덱스가 홀수인 위치에 있는 요소들 중 짝수만 출력하기

# 리스트 슬라이싱 이용
for i in int_list[1::2]:
    if i % 2 == 0 and i > 0:
        print(i)

# range 이용
for j in range(1, len(int_list), 2):
    if int_list[j] % 2 == 0 and int_list[j] > 0:
        print(int_list[j])


# 31.4-4 합 구하기
# 리스트 숫자의 합을 출력하는 프로그램을 작성하라.

# for loop을 이용했을 떄
tot_sum = 0
for i in int_list[::]:
    tot_sum += i
    print(i, tot_sum)
print("tot_sum:", tot_sum)

# fsum() 메소드를 이용했을 떄
import math
total = math.fsum(int_list)
print("total:", total)