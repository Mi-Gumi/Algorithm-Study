'''
비교수를 최소로 하기 위해 책상위의 뭉치 중에서 큰 뭉치는 최대한 나중에.
다시말해 크기가 작은 두 묶음을 골라 합쳐서 다시 책상위에 올림
카드 묶음이 하나가 될 때까지 반복
'''

from heapq import heappop, heappush
import sys; input = sys.stdin.readline

n = int(input())
q = []

total = 0
for _ in range() :
    heappush(q,int(input()))

while len(q) != 1 :
    plus = heappop(q) + heappop(q)
    total += plus
    heappush(q, plus)

print(total)