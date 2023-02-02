import sys
input = sys.stdin.readline

N = int(input())
scores = []
for i in range(N):
    scores.append(int(input()))

# 계단 별 점수의 최댓값을 담을 배열 생성
sum_scores = []

# N이 1이라면
if N == 1:
    # 첫번째 계단의 점수 출력
    print(scores[0])

# N이 2라면
elif N == 2:
    # 첫번째 계단과 두번째 계단 점수의 합 출력
    print(scores[0] + scores[1])

# N이 3이상 이라면
else:
    # 첫번째 계단 점수의 최댓값 저장
    sum_scores.append(scores[0])
    
    # 두번째 계단 점수의 최댓값 저장
    sum_scores.append(scores[0] + scores[1])

    # 세번째 계단 점수의 최댓값은 두번째 + 세번째 이거나 첫번째 + 세번째 이기에 더 큰값으로 설정
    if scores[1] + scores[2] >= scores[0] + scores[2]:
        sum_scores.append(scores[1] + scores[2])
    else:
        sum_scores.append((scores[0] + scores[2]))

    # 4번째 계단 이상부터
    for i in range(3, N):
        # 전 계단을 밟았을 경우의 최댓값은 현재 계단의 점수 + 전 계단의 점수 + 전전전 계단의 점수 최댓값
        prev = sum_scores[i - 3] + scores[i - 1] + scores[i]

        # 전전 계단을 밟았을 경우의 최댓값은 현재 계단의 점수 + 전전 계단의 점수 최댓값
        pprev = sum_scores[i - 2] + scores[i]

        # 전 계단을 밟았을 때와 전전 계단을 밟았을 때의 값중 큰값을 현재 계단의 점수 최댓값으로 추가
        if prev >= pprev:
            sum_scores.append(prev)
        else:
            sum_scores.append(pprev)

    # 맨 뒤 계단의 점수 최댓값 출력
    print(sum_scores[-1])