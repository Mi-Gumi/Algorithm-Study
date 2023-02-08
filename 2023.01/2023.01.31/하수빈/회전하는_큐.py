import sys
# collections 모듈의 deque 클래스 사용
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
# 원하는 순서를 담은 리스트 생성
order_list = list(map(int, input().split()))

# deque 객체 생성
queue = deque()
move = 0

# deque에 i추가
for i in range(1, N + 1):
    queue.append(i)

# order_list의 각 순서에 대해
for i in order_list:
    # deque안 i의 인덱스를 탐색
    idx = queue.index(i)

    # 인덱스가 0이라면
    if not idx:
        # 왼쪽 요소 pop
        queue.popleft()
    
    # deque의 길이 - 인덱스 보다 인덱스가 작다면
    elif len(queue) - idx > idx:
        # 왼쪽으로 회전
        queue.rotate(-idx)
        # 회전한 만큼 move 증가
        move += idx
        # 왼쪽 요소 pop
        queue.popleft()
    # deque의 길이 - 인덱스 보다 인덱스가 크다면
    else:
        # 오른쪽으로 회전
        queue.rotate(len(queue) - idx)
        # 회전한 만큼 move 증가
        move += (len(queue) - idx)
        # 왼쪽 요소 pop
        queue.popleft()

print(move)