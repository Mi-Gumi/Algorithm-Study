import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]

home.sort()

# 최소 거리
start = 1
# 최대 거리
end = home[-1] - home[0]
ans = 0

while start <= end:
    mid = (start + end) // 2
    now = home[0]
    cnt = 1

    for h in home:
        # 만약 현재 위치에서 공유기의 거리를 더한 것 보다 h가 크거나 같다면
        if h >= now + mid:
            # 공유기 설치
            cnt += 1
            # 현재위치 변환
            now = h
    
    # 설치한 공유기의 갯수가 C보다 크거나 같다면
    if cnt >= C:
        # 공유기의 거리를 늘려야함으로 start 변경
        start = mid + 1
        # ans 변경
        ans = mid
    # 설치한 공유기의 갯수가 C보다 작다면
    else:
        # 공유기의 거리를 줄여야함으로 end 변경
        end = mid - 1

print(ans)