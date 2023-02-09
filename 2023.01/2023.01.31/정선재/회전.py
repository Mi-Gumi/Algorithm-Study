import sys
n, m = map(int,sys.stdin.readline().split())
target = list(map(int,sys.stdin.readline().split()))
_list = list(range(1, n+1))
count = 0
for i in target:
    idx = _list.index(i)
    if idx == 0:
        _list.pop(0)
    elif len(_list) - idx >= idx:
        small_list = _list[:idx]
        big_list = _list[idx:]
        _list = big_list + small_list
        count += idx
        _list.pop(0)
        count += idx

    else :
        small_list = _list[:idx]
        big_list = _list[idx:]
        _list = big_list + small_list
        count += len(_list) - idx
        _list.pop(0)
        count += len(_list) - idx    


print(count)



