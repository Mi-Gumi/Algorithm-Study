import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 시작 시간이 빠른 순서대로 정렬
arr.sort()
ans = []

# 끝나는 시간 힙에 추가
heappush(ans, arr[0][1])
for i in range(1, N):
    # 현재 시작시간이 힙의 끝나는 시간보다 늦다면 교체
    if arr[i][0] >= ans[0]:
        heappop(ans)
    # 현재 시작시간이 힙의 끝나는 시간보다 빠르다면 새로운 강의실 추가
    heappush(ans, arr[i][1])

# 강의실 갯수 출력
print(len(ans))
