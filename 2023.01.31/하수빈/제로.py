# import sys
# input = sys.stdin.readline

# # K, 스택 선언 및 초기화
# K = int(input())
# stack = []

# # cmd가 0이라면 pop 아니라면 push
# for _ in range(K):
#     cmd = int(input())
#     if cmd == 0:
#         stack.pop()
#     else:
#         stack.append(cmd)

# print(sum(stack))

import sys
input = sys.stdin.readline
from queue import LifoQueue

# K, 스택, ssum 선언 및 초기화
K = int(input())

# LifoQueue 사용
stack = LifoQueue()
ssum = 0

# cmd가 0이라면 stack을 get 아니라면 stack에 cmd put
for _ in range(K):
    cmd = int(input())
    if cmd == 0:
        stack.get()
    else:
        stack.put(cmd)

# stack의 길이 만큼
for _ in range(stack.qsize()):

# get 한 값을 ssum에 합산
    ssum += stack.get()

print(ssum)