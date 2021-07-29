# 35.5-1  선형 검색 알고리즘 - 동일한 값을 여러 개 가지고 있는 1차원 리스트 검색하기
# 주어진 값과 동일한 값을 가지는 1차원 리스트를 검색하는 프로그램을 작성하라. 단, 리스트는 숫자값만을 가지고 있으며 동일한 값을 여러 개 가질 수 있다고 가정한다. 

import random

needle = random.randint(1, 5)
haystack = [None] * 5

for i in range(len(haystack)):
    haystack[i] = random.randint(1, 5)

found = False
for i in range(len(haystack)):
    if haystack[i] == needle:
        print(needle, "의 발견 위치", i)
        found = True

if found == False:
    print("동일한 값이 없습니다.")



# 35.5-2  동일한 영문 이름을 가지는 모든 사람의 영문 성 출력하기
# 20명의 영문 성과 영문 이름을 입력받아 각각 리스트에 저장하는 프로그램을 작성하라. 이 프로그램은 사용자에게 영문 이름을 물어보고, 해당 이름을 가지는 사람의 영문 성을 출력해야 한다.

PEOPLE = 20

first_name = ['Aidan', 'Rose', 'Gloria', 'Luna', 'Paul', 'Ricardo', 'Hector', 'Olive', 'Harmony', 'Francesca', 'Joey', 'Johnny', 'Scott', 'Martin', 'Tristin', 'Nicole', 'Eli', 'Conner', 'Ashley', 'Teresa']
last_name = ['Butler', 'Matthews', 'Hughes', 'Evans', 'Cox', 'Wara', 'Jenkins', 'Hicks', 'Crawford', 'Bryant', 'Ward', 'Watkins', 'Bennett', 'Simmons', 'Ward', 'Bailey', 'Murphy', 'Evans', 'Patterson', 'Matthews']
ran_name = first_name + ['Phoebe', 'Katelynn', 'Danna', 'Adrian', 'Kingston', 'scott', 'martin', 'alexis', 'peter', 'luna']

the_name = ran_name[random.randint(0, 29)]

found_name = False
for i in range(PEOPLE):
    if first_name[i].upper() == the_name.upper():
        print("first_name:", first_name[i], ", last_name:", last_name[i])
        print("i:", i)
        found_name = True

if found_name == False:
    print("어떤 사람도 발견하지 못했습니다.")



# 35.5-3  고유한 값들을 가지는 1차원 리스트 검색하기  
# 주어진 값과 동일한 값을 가지는 1차원 리스트를 검색하는 프로그램을 작성하라. 이 리스트는 숫자값만을 가지며, 고유하다고 가정한다. 

unique_list = [None] * 30
for i in range(len(unique_list)):
    unique_list[i] = random.randint(1, 100)

# 중복 제거: set -> list
unique_list = list(set(unique_list))
U_SIZE = len(unique_list)
print("unique_list:", unique_list, "// U_Size:", U_SIZE)


# 방법 A - break
needle_a = random.randint(1, 100)

found_a = False
for i in range(U_SIZE):
    if unique_list[i] == needle_a:
        print("needle_a:", needle_a, "의 위치:", i)
        found_a = True
        break

if found_a == False:
    print('needle_a와 동일한 값을 찾지 못했습니다.')

# 방법 B - flag
needle_b = random.randint(1, 100)

found_b = False
i = 0
while i < U_SIZE and found_b == False:
    if unique_list[i] == needle_b:
         found_b = True
         print("needle_b:", needle_b, "의 위치:", i)
         
    i += 1

if found_b == False:
    print('needle_b와 동일한 값을 찾지 못했습니다.')


# 방법 C - 사전-루프 구조(가장 효율적)
needle_c = random.randint(1, 100)

j = 0
while j < U_SIZE-1 and unique_list[j] != needle_c:
    j += 1

# 마지막 인덱스는 if문에서 실행
if unique_list[j] != needle_c:
    print('needle_c와 동일한 값을 찾지 못했습니다.')
else:
    print("needle_c:", needle_c, "의 위치:", j)

        


