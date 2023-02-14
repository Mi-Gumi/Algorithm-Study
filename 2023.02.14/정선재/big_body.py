N = int(input())
_list = [list(map(int, input().split()))for _ in range(N)]

ans = []
for i in range(N):
    count = 0
    for j in range(N):
        if _list[i][0] < _list[j][0] and _list[i][1] < _list[j][1]: 
            count += 1 
    ans.append(count + 1) 
 
for d in ans:
    print(d,end=" ")
