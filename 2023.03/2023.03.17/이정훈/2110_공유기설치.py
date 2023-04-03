import sys
input = sys.stdin.readline

N, C = map(int,input().rstrip().split())

house = [int(input()) for _ in range(N)]

# 정렬
house.sort()

# 집간의 최소거리와 최대거리를 기준
mindis = 1
maxdis = house[-1] - house[0]


while mindis <= maxdis  :
    cnt = 1
    mid = (mindis + maxdis)//2
    last = 0
    
    for i in range(1,N) :
        # 설치할 수 있다면 설치하고 기준을 옮김
        if mid <= house[i] - house[last] :
            last = i
            cnt += 1
    # 공유기 설치가 더 많이 되거나 같다면 설치거리를 늘려봄
    if cnt >= C :
        mindis = mid + 1
    # 적게 설치 되었다면 거리를 줄여야 함
    else :
        maxdis = mid -1
print(maxdis)

