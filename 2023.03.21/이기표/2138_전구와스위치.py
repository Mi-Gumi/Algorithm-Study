'''
i-1 , i , i+1 스위칭
첫 번째 전구를 누르고 시작하는 경우
첫 번째 전구를 누르지 않고 시작하는 경우
'''
import copy
N = int(input())
data = list(map(int, input()))
target = list(map(int, input()))

data_1 = copy.deepcopy(data)
data_2 = copy.deepcopy(data)

cnt_1 = 1
cnt_2 = 0

def switch(lst, cnt):
    for i in range(1, N):
        # 이전 전구와 비교했을 때 다른 상태인 경우
        if lst[i-1] != target[i-1]:
            cnt += 1
            lst[i - 1] = (lst[i - 1] + 1) % 2
            lst[i] = (lst[i] + 1) % 2
            # 마지막 인덱스인 경우를 고려
            if i == N-1:
                continue
            lst[i + 1] = (lst[i + 1] + 1) % 2
    # 일치하는 경우 카운트 반환
    if lst == target:
        return cnt
    else:
        return -1

data_1[0] = (data_1[0] + 1) % 2
data_1[1] = (data_1[1] + 1) % 2
# 첫 번째 스위치를 켜고 출발
cnt_1 = switch(data_1, cnt_1)
# 첫 번째 스위치를 껴지않고 출발
cnt_2 = switch(data_2, cnt_2)

# 두 가지 경우가 가능한 경우에서 최소값을 도출
if cnt_1 >= 0 and cnt_2 >= 0:
    print(min(cnt_1, cnt_2))
# 해당되는 값을 도출
elif cnt_1 >= 0 and not cnt_2 > 0:
    print(cnt_1)
elif not cnt_1 > 0 and cnt_2 >= 0:
    print(cnt_2)
# 해당되지 않는 경우
else:
    print(-1)






