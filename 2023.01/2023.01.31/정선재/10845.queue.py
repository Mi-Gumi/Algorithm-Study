import sys
n = int(sys.stdin.readline())
que = []
for _ in range(n):
    m = sys.stdin.readline().split()
    if m[0] == 'push':
        que.append(m[1])
    elif m[0] == 'pop':
        if len(que) != 0:
            print(que[0])
            que.pop(0)
        else :
            print(-1)
    elif m[0] == 'size':
        print(len(que))
    elif m[0] == 'empty':
        if len(que) != 0:
            print(0)
        else :
            print(1)
    elif m[0] == 'front':
        if len(que) == 0:
            print(-1)
        else :
            print(que[0])
    else :
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
