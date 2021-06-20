# 13. 다음 리스트를 생성하고 출력하는 프로그램을 작성하라.

n = 5
list_5 = [ [None] * n for i in range(5) ]

for i in range(n):
    for j in range(n):

        if i + j == n-1:
            list_5[i][j] = 5

        elif i + j <= 3:
            list_5[i][j] = 11

        else:
            list_5[i][j] = 88

print("list_5:", list_5)  


# 14. 다음 리스트를 생성하고 출력하는 프로그램을 작성하라.

list_25 = [ [None] * n for i in range(5) ]

for i in range(n):
    for j in range(n):

        if i + j == n-1:
            list_25[i][j] = 5

        elif i + j <= 3:
            list_25[i][j] = 11

        elif i + j >= 5:
            list_25[i][j] = 88

for k in range(n):

    list_25[k][k] = 0
    
print("list_25:", list_25)