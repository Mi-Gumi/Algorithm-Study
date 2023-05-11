# 단일 카드 뭉치, 합쳐진 카드 뭉치 중 작은 것들부터 합쳐나가기

from sys import stdin
from heapq import *

decks = int(stdin.readline())

heap = []

for _ in range(decks):
    heappush(heap, int(stdin.readline()))

comparison = 0

while len(heap) > 1:
    ca = heappop(heap)
    rd = heappop(heap)

    comparison += (ca + rd)

    heappush(heap, ca + rd)

print(comparison)
