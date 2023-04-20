import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
order = [[] for _ in range(N + 1)]
heap = []
cnt = [0] * (N + 1)
ans = []
for _ in range(M):
    A, B = map(int, input().split())
    # 문제 풀어야 하는 순서 추가
    order[A].append(B)
    # 먼저 풀어야 하는 문제 갯수 + 1
    cnt[B] += 1

for i in range(1, N + 1):
    # 먼저 풀어야 하는 문제가 없다면 힙에 추가
    if not cnt[i]:
        heappush(heap, i)

# 알아서 문제 번호가 작은 순서대로 pop됨으로 위상정렬 알고리즘 사용
while heap:
    now = heappop(heap)
    for next in order[now]:
        cnt[next] -= 1
        if not cnt[next]:
            heappush(heap, next)
    ans.append(now)

print(*ans)