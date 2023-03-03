import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 위치 순으로 기둥 정렬
arr.sort()
# 총 넓이
area = 0
# 현재 위치
now = 0

# 현재 위치가 마지막 기둥 전이라면 반복
while now < N - 1:
    # 현재 기둥부터 다음 기둥들 확인
    for i in range(now + 1, N):
        # 다음 기둥이 현재 기둥보다 크거나 같다면
        if arr[i][1] >= arr[now][1]:
            # 다음 기둥 위치에서 현재 기둥 위치를 뺀 값에 현재 기둥 높이를 곱한 값 추가
            area += arr[now][1] * (arr[i][0] - arr[now][0])
            # 현재 위치 변경
            now = i
            break
    # 현재 기둥 보다 큰 기둥이 없다면
    else:
        # 현재 기둥 다음으로 큰 기둥 높이와 위치 저장
        n_max = max(arr[now + 1:], key=lambda x:x[1])
        # 현재 기둥 높이를 더하고 다음으로 큰 기둥 위치에서 현재기둥 위치와 1을 뺀 값에 다음으로 큰 기둥 높이를 곱한 값 추가
        area += arr[now][1] + (n_max[0] - arr[now][0] - 1) * n_max[1]
        # 현재 위치 변경
        now = arr.index(n_max)
# 마지막 기둥의 높이 추가
area += arr[now][1]

print(area)