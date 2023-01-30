N, K = map(int,input().split())

ans = []
linked_list = []
if N == 1 :
    linked_list = [[0, 0]]
else :
    for n in range(N) :
        if n == 0 :
            linked_list.append([N-1,n+1])
        elif n != N-1 :
            linked_list.append([n-1,n+1])
        else :
            linked_list.append([n-1,0])

count = 0
idx = K-1

while len(ans) != N :
    next_node = linked_list[idx][1]
    
    if count % (K) == 0:
        ans.append(idx+1)
        before_node = linked_list[idx][0]
        linked_list[before_node][1] = next_node
        linked_list[next_node][0] = before_node

    idx = next_node
    count += 1
rst = '<'+', '.join(list(map(str,ans)))+'>'
print(rst)
        