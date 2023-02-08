import sys
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    cmdin = input().strip().split(' ')
    cmd = cmdin[0]
    if cmd == 'push' :
        queue.append(cmdin[1])
    elif cmd == 'pop' :
        if queue :
            print(queue.pop(0))
        else :
            print(-1)
    elif cmd == 'front' :
        if queue :
            print(queue[0])
        else :
            print(-1)
    elif cmd == 'back' :
        if queue :
            print(queue[-1])
        else :
            print(-1)
    elif cmd == 'size' :
        print(len(queue))
    elif cmd == 'empty' :
        if queue :
            print(0)
        else :
            print(1)
        
    
        
