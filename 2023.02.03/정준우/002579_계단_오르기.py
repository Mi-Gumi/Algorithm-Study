# 마지막 계단은 무조건 밟아야하니, 어떻게 올라가는가보다는 여기까지 어떻게 올라왔는가

stairs = int(input())

scores = [int(input()) for _ in range(stairs)]

# 해당 인덱스까지의 점수를 담을 계단 수만큼의 요소를 가진 리스트 생성
scores_until_now = [0] * stairs

# 계단이 3개 이상이라 여러 경우를 고려해야할 때
if len(scores) >= 3:
    # 첫번째, 두번째 계단까지는 직접 계산해서 값 얻고
    scores_until_now[0] = scores[0]
    scores_until_now[1] = scores[0] + scores[1]
    # 3번째 계단부터는 점화식 사용
    # 해당 계단까지 도달할 수 있는 경우들 중 최대값 뽑아내기
    # 3번째 계단에서 한 계단을 건너뛴 경우와, 두 계단을 연속으로 올라간 경우의 두 가지 식을 비교해 그 중 점수가 높은 것을 뽑아냄
    for i in range(2, stairs):
        scores_until_now[i] = max(scores_until_now[i-2] + scores[i], scores_until_now[i-3] + scores[i-1] + scores[i])
    # 그렇게 나온 점수의 마지막을 출력
    print(scores_until_now[-1])

else:
    # 계단이 3개 미만이라면, 경우 고려할 것 없이 계단의 점수 더한 것이 최대값
    print(sum(scores))