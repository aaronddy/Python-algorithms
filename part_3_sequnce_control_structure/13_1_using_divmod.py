# 13.1-1  정수 나눗셈의 몫과 나머지 계산하기

# code 1
num1 = int(input("첫번째 숫자를 입력하세요. "))
num2 = int(input("두번째 숫자를 입력하세요. "))

q = num1 // num2
r = num1 % num2

print("방법 1", "몫:", q, "나머지", r)

# code 2. divmod 사용하기

q, r = divmod(num1, num2)

print("방법 2", "몫:", q, "나머지", r)



# 13.1-2  자릿수값의 총합 계산하기

# code 1. 몫만 이용하기
number = int(input("네 자리 정수를 입력하라."))

thou = number // 1000
hund = (number - thou*1000) // 100
ten = (number - thou*1000 - hund*100) // 10
one = (number -thou*1000 - hund*100 - ten*10) // 1

total_sum = thou + hund + ten + one

print("code1_sum: ", total_sum)


# code 2. 몫과 나머지 이용하기

digit1 = number // 1000
r = number % 1000

digit2 = r // 100
r = r % 100

digit3 = r // 10
digit4 = r % 10

total_digit = digit1 + digit2 + digit3 + digit4

print("code2_sum: ", total_digit)


# code 3. divmod 이용하기

div1, mod1 = divmod(number, 1000)
div2, mod2 = divmod(mod1, 100)
div3, div4 = divmod(mod2, 10)

total_div = div1 + div2 + div3+ div4

print("code3_sum: ", total_div)


# code 4. 끝자리 수부터 구하기

num4 = number % 10
r = number // 10

num3 = r % 10
r = r // 10

num2 = r % 10
num1 = r // 10

total_num = num1 + num2 + num3 + num4
print("code4_sum: ", total_num)



