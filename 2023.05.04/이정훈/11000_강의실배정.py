import sys; input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())

suup =  []

for _ in range(n) :
    start, end =  map(int,input().split())

    suup.append((start, end))

suup.sort(key=lambda x : x[0])

room = []
heappush(room, 0 )
for i in range(n) :
    # 제일 먼저 가용가능한 강의실의 종료 시간
    # end = heappop(room)
    # if suup[i][0] >= end :
    # print(room)
    if suup[i][0] >= room[0] :
        heappop(room)
        heappush(room, suup[i][1])
    else :
        # heappush(room, end)
        heappush(room, suup[i][1])

print(len(room))

# heapq은 정렬되어 있는 상태

