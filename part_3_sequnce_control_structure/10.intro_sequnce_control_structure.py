# 10.1-1  평행사변형 면적 계산

base = float(input('밑변을 입력하세요'))
height = float(input('높이를 입력하세요'))

square = base * height
print("평행사변형 면적은?", square)



# 10.1-2  원의 면적 계산

PI = 3.14159
radius = float(input('원의 반지름을 입력하세요'))

area = PI * radius ** 2
print("원의 면적은?", area)



# 10.1-3  연비 계산
# MPG = 주행한 총 마일 / 소비된 휘발유(gallon)

miles = float(input("주행한 총 마일은?"))
gallon = float(input("소비된 휘발유 양은?"))

mpg = miles / gallon
print("자동차 연비는(MPG)?", mpg)




# 10.1-4  주행 거리 계산

u = 0
a = float(input("가속도는?"))
t = float(input("주행 시간은?"))

s = u + (0.5 * a * t ** 2)
print("주행 거리(m)는", s)



# 10.1-5  화씨 온도값을 켈빈 온도값으로 변환

f = float(input("화씨 온도값은?"))

kelvin = (f + 459.67) / 1.8
print('켈빈 온도값은: ', kelvin)



# 10.1-6  판매세 계산하기

tax = 0.19
values = float(input("상품의 세전 가격은?"))
sales_tax = tax * values

price = values + sales_tax
print("상품의 세후 가격은?", price)



# 10.1-7  할인 가격 계산하기

discount = int(input("할인율은?(1-100)")) / 100
product_price = float(input("상품 가격은?"))

discount_amount = discount * product_price
discount_product_price = product_price - discount_amount

print("할인이 적용된 상품 가격은?", discount_product_price)



# 10.1-8  팁과 판매세가 포함된 최종 음식값 계산하기

TIP = 0.1
VAT = 0.07

base_price = float(input("음식값은 얼마인가?"))

price_TIP = base_price * TIP
price_VAT = base_price * VAT

total_price = base_price + price_TIP + price_VAT
print("최종 음식값은?", total_price)



# 10.1-9  총 전기요금 계산하기

PAY_PER_KWH = 600
VAT = 0.2

kwh = float(input("한 달간 사용한 전력 소비량은?(kwh 단위)"))

pay_kwh = kwh * PAY_PER_KWH
pay_vat = pay_kwh * VAT

total_pay = pay_kwh + pay_vat
print("총 전기요금은?", total_pay)



# 10.1-10  1월 1일부터 경과된 총 일 수 계산하기

m = int(input("월을 입력하세요"))
d = int(input("일을 입력하세요"))

month = (m - 1) * 30
day = d - 1

total_days = month + day
print("1월 1일로부터 현재", total_days, "일이 경과되었습니다.")
