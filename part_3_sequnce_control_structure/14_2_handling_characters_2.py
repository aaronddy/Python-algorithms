# 14.4-1  이름 순서 교환하기
# 이름과 성을 문자열로 입력받아 이름과 성 순서를 서로 바꾸는 프로그램 작성

full_name = input("이름과 성을 영어로 입력하라: ")

# find() 를 이용해 " "의 인덱스 찾기
find_space = full_name.find(" ")
print("space index:", find_space)

front_name = full_name[:find_space]
back_name = full_name[find_space+1:]

print(front_name, back_name)

reverse_name = back_name + " " + front_name
print("순서가 바뀐 이름은?", reverse_name)



# 14.4-2  로그인 ID 생성하기
# 사용자의 성(last name)을 입력받고, 성의 첫 번째 네 개의 문자(소문자로 변경)와 그 뒤에 세자리 랜덤 정수로 이루어진 로그인 ID를 생성하는 프로그램 작성

import random

last_name = input("성을 영어로 입력하라: ")

last_name = last_name.lower()
print("소문자로 변경:", last_name)

# 100과 999 사이의 랜덤 정수를 얻은 후, string으로 데이터 타입 변경(정수로 받으면 타입 에러 발생)
random_num = str(random.randrange(100, 1000))

user_ID = last_name+random_num
print("생성된 로그인 ID는", user_ID, " 입니다")



# 14.4-3  랜덤 단어 생성하기
# 다섯 개의 문자로 이루어진 랜덤 단어를 출력하는 프로그램 작성

import string

alphabet = string.ascii_lowercase

random_word_a = alphabet[random.randrange(26)]+      \
                alphabet[random.randrange(26)]+      \
                alphabet[random.randrange(26)]+      \
                alphabet[random.randrange(26)]+      \
                alphabet[random.randrange(26)]




print(random_word_a)