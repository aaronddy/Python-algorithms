rdn_list = [2, 4, 10, 9, 11, 25, 3, -1, 8, 105, -23]

triple_lst = rdn_list * 3
print(triple_lst)


# 8. 각 숫자를 세제곱하여 출력하는 파이썬 프로그램을 작성하라

for i in range(len(rdn_list)):
    print("8_result:", rdn_list[i] ** 3)


# 9. 각 숫자를 제곱하여 역순으로 출력하는 파이썬 프로그램을 작성하라

for i in rdn_list[::-1]:
    print("9_result:", i ** 2)


# 10. 5로 정확히 나눠지는 정수만을 역순으로 출력하는 파이썬 프로그램을 작성하라.

for i in rdn_list[::-1]:
    if i % 5 == 0:
        print("10_result:", i)


# 11. 짝수나 10보다 큰 수들을 출력하는 파이썬 프로그램을 작성하라.

for i in rdn_list:
    if i % 2 == 0 or i > 10:
        print("11_result:", i)


# 12. 양수들의 합을 계산하고 출력하는 파이썬 프로그램을 작성하라.

even_sum = 0
for i in rdn_list:
    if i % 2 == 0:
        even_sum += i
        print(i, even_sum)

print("12_result:", even_sum)


# 13. 두 자릿수 정수들의 합을 계산하고 출력하는 파이썬 프로그램을 작성하라.

two_digits_sum = 0
for i in rdn_list:
    if i >= 10 and i <= 99:
        two_digits_sum += i
        print(i, two_digits_sum)

print("13_result:", two_digits_sum)


# 14. 양수의 합과 음수의 합을 각각 계산하여 출력하는 파이썬 프로그램을 작성하여라.

sum_pos = 0
sum_neg = 0

for i in rdn_list:
    if i > 0:
        sum_pos += i
    elif i < 0:
        sum_neg += i

print("14_result:", sum_pos)
print("14_result:", sum_neg)


# 17. 단어 리스트 중에 'w'가 최소 두 번  이상 나오는 단어를 출력해 주는 파이썬 프로그램을 작성하여라.

word_lst = ['word', 'wow', 'hospital', 'tiger', 'wreck', 'boil', 'www', 'whisperw']
w_lst = []

for i in word_lst:
    w_count = 0
    
    for j in i:   
        if j == 'w':
            w_count += 1

    if w_count >= 2:
        w_lst.append(i)

print("17_result:", w_lst)