# 35.3-1 가장 깊은 호수 찾기
# 20개 호수에 대한 깊이 값을 입력받고, 가장 깊은 호수의 깊이값을 출력하는 프로그램을 작성하라.
import random

SIZE = 20
lake_depth = []

for i in range(SIZE):
    depth = random.randint(1000, 2000)
    lake_depth.append(depth)

print("lake_depth:", lake_depth)

# 방법 A
maximum = -1
for i in lake_depth:
    if i > maximum:
        maximum = i

print("maximum:", maximum)


# 방법 B
the_depth = max(lake_depth)
print("the_depth:", the_depth)


# 35.3-2 가장 깊은 호수 찾기
# 20개 호수의 깊이 값을 입력받고, 가장 깊은 호수의 이름을 출력하는 프로그램을 작성하라.

lake_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
depth_name = ''
depth_long = -1

for i in range(SIZE):
    if lake_depth[i] > depth_long:
        depth_long = lake_depth[i]
        depth_name = lake_name[i]

print("depth_name:", depth_name, "/ depth_long:", depth_long)
