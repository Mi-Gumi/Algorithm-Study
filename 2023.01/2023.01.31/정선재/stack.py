import sys
n = int(sys.stdin.readline())
_list = []
for _ in range(n):
    m = sys.stdin.readline().split()
    if m[0] == 'push':
        _list.append(m[1])
    elif m[0] == 'pop':
        if len(_list) != 0:
            print(_list[-1])
            _list.pop()
        else :
            print(-1)
    elif m[0] == 'size':
        print(len(_list))
    elif m[0] == 'empty':
        if len(_list) == 0:
            print(1)
        else:
            print(0)
    elif m[0] == 'top':
        if len(_list) != 0:
            print(_list[-1])
        else:
            print(-1)
