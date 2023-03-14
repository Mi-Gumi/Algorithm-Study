import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
wait = list(map(int, input().split()))
# pop하지 않기위해 reverse
wait.reverse()
q = deque([0] * w)
t = 0

# 큐에 요소가 없을 때 까지
while q:
    # 시간 + 1
    t += 1
    # 큐 왼쪽요소 제거
    q.popleft()
    # 대기 트럭이 남아있다면
    if wait:
        # 큐의 합 + 대기 트럭이 L보다 크다면
        if sum(q) + wait[-1] > L:
            # 트럭 추가 x
            q.append(0)
        # 아니라면 트럭 추가
        else:
            q.append(wait.pop())

print(t)