# 29.6  루프 제어 구조를 가진 일반 형태의 프로그래밍 예제

# 29.6-1  0에서 100도의 화씨 온도를 켈빈 온도로 변환하기
# 0부터 100도까지의 화씨 온도와 이에 대응하는 켈빈 온도를 출력하는 파이썬 프로그램을 작성하라. 0.5도씩 화씨 온도를 증가시키며, 변환 수식은 다음과 같다.(1.8 * 켈빈 온도 = 화씨 온도 + 459.67)

for i in range(201):

    i = i / 2
    k_temp = (i + 459.67) / 1.8
    print("화씨 온도:", i/2)
    print("켈빈 온도:", k_temp)


# 29.6-2  체스판 위의 밀알
# 체스판 위에 밀알 하나를 첫 번째 사각형에, 두 번째 사각형에는 밀알 두 개, 세 번째 사각형에는 밀알 네 개를 배치하도록 사각형마다 밀알을 놓아야 한다고 해 보자(이전 사각형의 두 배를 현재 사각형에 배치). 체스판에 얼마나 많은 밀알이 놓아져야 하는가?

total = 0

for i in range(1, 65):
    i = 2 ** (i-1)
    total += i
    
print("전체 밀알 수:", total)


# 29.6-4  메시지가 회문인가?
# 회문은 앞으로 읽어도 뒤로 읽어도 서로 동일한 단어나 문장이다. 사용자로부터 단어나 문장을 입력받은 후, 그 단어나 문장이 회문인지 아닌지의 여부를 검사하는 파이썬 프로그램을 작성하라.

message = input("문장을 입력하라").lower()

# 공백, 쉼표, 구두점, 물음표 등을 제거
message_clean = ""

for letter in message:
    if letter not in " ,.?!":
        message_clean += letter
print(message_clean)

# 문자열 개수 파악
m_len = int(len(message_clean) // 2)
same = 0

for i in range(m_len):

    left_letter = message_clean[i]
    right_letter = message_clean[-(i+1)]
    
    if left_letter == right_letter:
        print("same")
        same += 1
    else: break

if same == m_len:
    print(same)
    print("회문입니다")
else:
    print("회문이 아닙니다.")
    


