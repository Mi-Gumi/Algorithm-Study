T = int(input())

N = int(input())

net = dict()
is_passed = [False for _ in range(T)]
for i in range(N):
    c1, c2 = map(int, input().split())    
    if not net.get(c1) or not net.get(c2):
        net.setdefault(c1,set())
        net.setdefault(c2,set())
    net[c1].add(c2)
    net[c2].add(c1)
    

cnt = -1
def dfs(warm):
    global cnt
    if is_passed[warm - 1] == True:
        return
    if is_passed[warm - 1] == False:
        cnt += 1
        is_passed[warm - 1] = True
        
    if net.get(warm):
        connected = list(net[warm])
    else:
        return
    
    for com in connected:
        dfs(com)
dfs(1)
print(cnt)
