import sys
from collections import deque
input = sys.stdin.readline

def deque_function(command, dual_que):
    pass
    if command[0][:4] == 'push':
        front_back = command[0].split('_')
        if front_back[1] == 'back':
            dual_que.append(command[1])
        else:
            dual_que.appendleft(command[1])

    elif command[0][:3] == 'pop':
        front_back = command[0].split('_')
        if front_back[1] == 'back':
            if not dual_que:
                print(-1)
            else:
                pop_num = dual_que.pop()
                print(pop_num)
        else:
            if not dual_que:
                print(-1)
            else:
                pop_num = dual_que.popleft()
                print(pop_num)
    elif command[0] == 'size':
        print(len(dual_que))
    elif command[0] == 'empty':
        if not dual_que:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not dual_que:
            print(-1)
        else:
            print(dual_que[0])
    elif command[0] == 'back':
        if not dual_que:
            print(-1)
        else:
            print(dual_que[-1])


T = int(input())
dual_que = deque()
for t in range(T):
    command = input().split()
    deque_function(command, dual_que)