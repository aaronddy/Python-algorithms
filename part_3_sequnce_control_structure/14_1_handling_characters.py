# 14.2-1  자릿수값의 총합 계산하기

number = input("세 자리 정수를 입력하라: ")
print("넘버의 데이터 타입은? ", type(number))   # str

a, b, c = number
result = int(a) + int(b) + int(c)

print("자릿수값의 합: ", result)



# 14.3-1  문자열을 역순으로 출력하기

# code1
cha = input('네 개의 문자를 가진 문자열을 입력하라: ')

l1 = cha[0]
l2 = cha[1]
l3 = cha[2]
l4 = cha[3]

letters = l4+l3+l2+l1

print("code1_letters:", letters)


# code2

m, n, o, p = cha

letters2 = p+o+n+m

print("code2_letters:", letters2)


# code3

letters3 = cha[::-1]
print("code3_letters:",letters3)
