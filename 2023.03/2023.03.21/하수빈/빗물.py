import sys
input = sys.stdin.readline

H, W = map(int, input().split())
arr = list(map(int, input().split()))
# 총량
mount = 0
# 현재 위치
now = 0

# 현재 위치가 마지막 블록 전이라면 반복
while now < W - 1:
    # 현재 블록의 다음 블록들 확인
    for i in range(now + 1, W):
        # 다음 블록이 현재 블록보다 크거나 같다면
        if arr[i] >= arr[now]:
            # 현재 블록과 현재 블록보다 높은 블록 사이의 블록들에 고인 빗물의 양 합산
            for j in range(now + 1, i):
                mount += arr[now] - arr[j]
            # 현재 위치 변경
            now = i
            break
    # 현재 블록 보다 큰 블록이 없다면
    else:
        # 현재 블록 다음으로 큰 블록 위치 저장
        tmp = arr[now + 1:]
        max_idx = tmp.index(max(tmp)) + now + 1
        # 현재 블록과 현재 블록 다음으로 높은 블록 사이의 블록들에 고인 빗물의 양 합산
        for i in range(now + 1, max_idx):
            mount += arr[max_idx] - arr[i]
        # 현재 위치 변경
        now = max_idx

print(mount)