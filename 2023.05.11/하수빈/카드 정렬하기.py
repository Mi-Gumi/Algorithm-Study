import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    heappush(heap, int(input()))
ans = 0

while len(heap) != 1:
    # 가장 작은 카드 뭉치 두개 선택
    a = heappop(heap)
    b = heappop(heap)
    ssum = a + b
    # ans 에 합산
    ans += ssum
    # 합산한 카드 뭉치 추가
    heappush(heap, ssum)

print(ans)