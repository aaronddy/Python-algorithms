# 33.7 리스트의 유용한 함수와 메서드

# 1. 요소 개수 세기 
lst = [3, 6, 10, 12, 4, 2, 1, 98]

print("length:", len(lst))
print("length_part:", len(lst[2:5]))


# 2. 최댓값 찾기
print("max:", max(lst))
print("max_part:", max(lst[1:5]))

lst2 = [[4, 10, 2], \
        [33, 12, 90], \
        [9, 21, 3]
       ]

print("max_lst2:", max(lst2[1]))

words = ['Apollo', 'Hermes', 'Athena', 'Aphrodite', 'Dionysus']

print("max_words:", max(words))  # 문자열의 최대값은 오름차순으로 가장 뒤에 배치되는 문자열


# 3. 최솟값 찾기
print("min:", min(lst))
print("min_part:", min(lst[2:6]))
print("min_lst2:", min(lst2[0]))
print("min_words:", min(words))


# 4. 리스트 정렬하기
# sort() 메서드는 기존의 리스트를 정렬, sorted() 함수를 통해 초기 리스트는 그대로 두고 새롭게 정렬된 리스트를 생성

# 오름차순
lst.sort()
print("sort_lst:", lst)

# 내림차순
lst.sort(reverse=True)
print("sort_reverse:", lst)

# 마지막 열 정렬
lst2[2].sort()
print("lst2:", lst2)

words.sort(reverse=True)
print("sort_words:", words)


# sorted() 함수 사용하기
sorted_lst = sorted(lst)
print("sorted_lst:", sorted_lst)

sorted_lst2 = sorted(lst2[0])
print("sorted_lst2[0]:", sorted_lst2)

sorted_words = sorted(words, reverse=True)
print("sorted_words:", sorted_words)