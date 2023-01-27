# 시간 제한에 걸려, N에서 주어진 숫자들을 리스트가 아닌 세트로 변환해주며 중복 숫자 모두 제거

N = int(input())
N_set = set(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

for i in range(M):
    if M_list[i] in N_set:
        print(1)
    else:
        print(0)