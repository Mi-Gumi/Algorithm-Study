import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = list(map(int,sys.stdin.readline().split()))
    m = list(map(int,sys.stdin.readline().split())) 
    _list = []
    ans = []
    max_m = sorted(m, reverse=True)
    for i in range(n[0]):
        _list.append([m[i],i])
    j = 1
    while j :
        if not _list:
            break
        if _list[0][0] == max_m[0]:
            pop_li = _list.pop(0)
            ans.append(pop_li)
            max_m.pop(0)
        elif _list[0][0] != max_m[0]:
            _list.append(_list[0])
            _list.pop(0)     

    for k in range(len(ans)):
        if ans[k][1] == n[1]:
            print(k+1)





