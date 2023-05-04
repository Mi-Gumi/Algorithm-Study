'''
1. 입력 받은 강의 시간을 정렬
2. 우선순위 큐를 사용하여 강의 시간을 서로 비교해가며 강의를 push, pop
3. 최종 heap에 남아있는 개수가 강의실의 개수
-> 우선순위 큐를 사용하지 않는다면 매번 반복되는 정렬과 탐색으로 인해 시간초과 발생
'''
import heapq

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
heap = []
for i in range(N):
    if heap:
        if heap[0] <= lst[i][0]: # heapq에 들어있는 값 중 가장 작은 값과 비교하여 강의 진행이 가능하면 pop, push
            heapq.heappop(heap)
            heapq.heappush(heap, lst[i][1])
        # 강의가 불가능하면 push
        else:
            heapq.heappush(heap, lst[i][1])
    else:
        heapq.heappush(heap, lst[i][1])
print(len(heap))