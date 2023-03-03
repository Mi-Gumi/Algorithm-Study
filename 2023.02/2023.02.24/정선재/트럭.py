import sys
input = sys.stdin.readline
n, w, l = map(int,input().split())
_list = list(map(int,input().split()))
l_list = []
val = []
cnt = 0
flag = 1
while flag:
    cnt += 1
    if len(_list) == 0 and len(l_list) == 0:
        flag = 0
        break
    if len(_list) != 0:
        if sum(l_list) + _list[0] <= l and len(l_list) < w:
            l_list.append(_list.pop(0))
            val.append(w)
        
    if len(l_list) != 0:    
        for i in range(len(val)):
            val[i] = val[i]-1
    
        if val[0] == 0:
            l_list.pop(0)
            val.pop(0)
    



print(cnt)