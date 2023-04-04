import sys
input = sys.stdin.readline
N, C = map(int, input().split())
lst = []
for _ in range(N):
    tmp = int(input())
    lst.append(tmp)
lst.sort() # 집 위치를 오름차순으로 정렬

start = 0 # 최소 거리 간격
end = lst[-1] - lst[0] # 최대 거리 간격
ans = mid = 0
while start <= end:
    # 집 사이의 간격
    mid = (start+end)//2
    # 최대거리를 유지해야하기 때문에 첫 설치위치는 첫번째 값
    target = lst[0]
    cnt = 1 # 첫번째 값이 먼저 설치되었기 때문에 횟수 1 증가

    for i in range(1, N):
        if target+mid <= lst[i]: # 설치위치+간격보다 집 위치가 큰 경우
            cnt += 1 # 설치횟수 증가
            target = lst[i] # 설치위치 최신화

    if C <= cnt: # 설치횟수가 더 커진경우
        start = mid + 1 # 탐색 범위 조정
        ans = mid # 현재까지의 인접한 거리 중 최대값

    else: # 설치횟수가 더 작은 경우
        end = mid - 1 # 탐색 범위 조정
print(ans)

