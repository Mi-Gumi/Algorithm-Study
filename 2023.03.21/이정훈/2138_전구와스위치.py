N = int(input())

start = list(map(int, input()))
target = list(map(int, input()))

start_with_first = start.copy()
# 스위치를 킬 때 영향을 주는 범위 -> i-1, i, i+1
# 스위치는 무조건 키거나 끄거나 2번 이상 키는 경우는 없음

# 따라서 처음부터 순회하면서 i-1번째 전구가 다를 경우 i번째의 스위치를 켜서 똑같이 맞춰줌
# 하지만 첫번째 스위치는 키고 끄냐에 따라 결과가 크게 달라짐
ans = [-1]
# 처음 스위치를 키지 않고 
cnt1 = 0
for i in range(1, N-1):
    if start[i-1] != target[i-1]:
        for j in range(i-1, i+2):
            start[j] = (start[j] + 1) % 2
        cnt1 += 1
if start[N-2] != target[N-2]:
    for j in range(N-2, N):
        start[j] = (start[j] + 1) % 2
    cnt1 += 1

if start == target:
    ans.append(cnt1)

# 처음 스위치를 키고
cnt2 = 1
for j in range(0, 2):
    start_with_first[j] = (start_with_first[j] + 1) % 2
for i in range(1, N-1):
    if start_with_first[i-1] != target[i-1]:
        for j in range(i-1, i+2):
            start_with_first[j] = (start_with_first[j] + 1) % 2
        cnt2 += 1
if start_with_first[N-2] != target[N-2]:
    for j in range(N-2, N):
        start_with_first[j] = (start_with_first[j] + 1) % 2
    cnt2 += 1

if start_with_first == target:
    ans.append(cnt2)

# 답 도출
if len(ans) == 1:
    print(ans[0])
else:
    ans.sort()
    print(ans[1])
