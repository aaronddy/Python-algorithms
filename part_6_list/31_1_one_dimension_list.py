# 31.2 1차원 리스트에서 값을 불러오는 방법

# 0보다 작은 인덱스는 리스트의 마지막 요소부터 세기 시작한다. 
grades = ["B+", "A+", "A", "C-"]
print(grades[-1])
print(grades[-2])
print(grades[-3])
print(grades[-4])


# slicing
print(grades[0:4:2])
print("역순 슬라이싱 1step", grades[::-1])
print("역순 슬라이싱 2step", grades[-2::-2])
print("역순 슬라이싱 3step", grades[-2::-3])


# 31.2-2 존재하지 않는 인덱스 사용하기

'''
주의: 리스트를 사용할 때는 존재하지 않는 요소를 참조해서는 안 된다.
print(grades[100])  => 이 예제는 존재하지 않는 요소를 참조하고 있다. 
'''

# 31.3 1차원 리스트에 사용자로부터 입력받은 값 추가하기
# 키보드로부터 값을 입력받은 후 그 값을 변수에 할당하지 않고 리스트의 특정 위치에 할당할 수 있다. 

test = [None] * 4
test[0] = input()
test[1] = input()
test[2] = input()
test[3] = input()
print("test:", test)

test_2 = []
test_2.append(input("첫 번째 사람의 이름을 입력하여라:"))
test_2.append(input("두 번째 사람의 이름을 입력하여라:"))
test_2.append(input("세 번째 사람의 이름을 입력하여라:"))
test_2.append(input("네 번째 사람의 이름을 입력하여라:"))
print("test2:", test_2)

