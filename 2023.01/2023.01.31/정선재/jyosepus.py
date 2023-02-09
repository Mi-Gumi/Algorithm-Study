import sys
n, m = map(int,sys.stdin.readline().split())
_list = list(range(1, n+1))
front_list = []
back_list = []
ans_list = []
while len(ans_list) != n :
    front_list = _list[:m-1]
    back_list = _list[m:]
    ind =_list[m-1]
    ans_list.append(ind)
    _list = (back_list + front_list ) * 2
    for _ in range(_list.count(ind)) :
        _list.remove(ind)


print(ans_list)
