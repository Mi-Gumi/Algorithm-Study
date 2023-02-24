import sys
input = sys.stdin.readline

_list = list(input().strip())
N = int(input())
sub_list = []
for i in range(N):
    a = list(input().strip().split())


    if a[0] == 'L':
        if len(_list) != 0: 
            sub_list.append(_list[-1])
            _list.pop()
    
    elif a[0] == 'D':
        if len(sub_list) != 0:
            _list.append(sub_list[-1])
            sub_list.pop()
    elif a[0] == 'B':
        if len(_list) != 0 :
            _list.pop()
    
    elif a[0] == 'P':
        _list.append(a[1])

sub_list = sub_list[::-1]
ans = _list + sub_list
print(*ans, sep = '')

