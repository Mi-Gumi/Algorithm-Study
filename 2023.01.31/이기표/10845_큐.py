import sys
input = sys.stdin.readline

def que_function(command, que):
    if command[0] == 'push':
        que.append(int(command[1]))
    elif command[0] == 'pop':
        if que:
            print(que.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] ==  'empty':
        if que:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif command[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])

T = int(input())
que = []
for t in range(T):
    command = input().split()
    que_function(command, que)
