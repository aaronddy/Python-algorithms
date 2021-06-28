# 12.
a = [[9, 9, 2, 6], [4, 1, 10, 11], [12, 15, 7, 3]]

to_lst = [ [None] for i in range(12)]
k = 0

for i in range(3):
  for j in range(4):
    to_lst[k] = a[i][j]
    k += 1

print("to_lst:", to_lst)


# 13.
b = [16, 12, 3, 5, 6, 9, 18, 19, 20]

to_lst2 = [ [None] * 3 for i in range(3) ]
k = 0

for i in range(3):
  for j in range(3):
    to_lst2[i][j] = b[k] 
    k += 1

print("to_lst2:", to_lst2)


# 10.
import math

currency = ['영국 파운드', '유로', '캐나다 달러', '호주 달러']
exchange_rt = [[1.579, 1.577, 1.572, 1.580, 1.584], \
                [1.269, 1.270, 1.265, 1.240, 1.255], \
                [0.895, 0.899, 0.884, 0.888, 0.863], \
                [0.811, 0.815, 0.822, 0.829, 0.819]]

exchange_rt_mean = []

for i in range(len(exchange_rt)):
    total = 0

    for j in range(len(exchange_rt[i])):
        total += exchange_rt[i][j]

    total /= len(exchange_rt[i])
    total = round(total, 3)
    exchange_rt_mean.append(total)

print("mean_lst:", exchange_rt_mean)

USD = float(input("미국 달러를 입력하시오."))
for i in range(len(exchange_rt_mean)):   
    print(currency[i], "환전값:", round(USD * exchange_rt_mean[i], 3))