N, M = map(int,input().split())
friends = [set() for _ in range(N)]
is_travel = [False]*N

for _ in range(M):
    a, b = map(int,input().split())
    friends[a].add(b)
    friends[b].add(a)

def bt(depth, now, end=5):
    if depth == end:
        return True
    
    for friend in friends[now]:
        if is_travel[friend] : continue
        is_travel[friend] = True
        trigger = bt(depth+1, friend)
        if trigger : return True
        is_travel[friend] = False

for i in range(N):
    if bt(0,i):
        print(1)
        break
else:
    print(0)