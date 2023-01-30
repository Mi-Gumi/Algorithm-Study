N , M = map(int,input().split())

dequeue = list(range(1,N+1))
Mlist = list(map(int,input().strip().split()))
count = 0
for target in Mlist :
    while True :
        idx = dequeue.index(target)
        if dequeue[0] == target:
            dequeue.pop(0)
            break
        
        else :
            if idx >= len(dequeue)/2 :
                count += len(dequeue[idx:])
            else :
                count += len(dequeue[:idx])
            dequeue = dequeue[idx:] + dequeue[:idx]
print(count)
                