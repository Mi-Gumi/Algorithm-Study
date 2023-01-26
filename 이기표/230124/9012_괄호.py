import sys
input = sys.stdin.readline

T = int(input())
# 후입선출 스택
for t in range(T):
    vps = input()
    vps_li = []
    for v in vps:
        if v == '(':
            vps_li.append(v)
        elif v == ')':
            if not vps_li:
                vps_li.append(v)
            elif ')' in vps_li:
                vps_li.append(v)
            else:
                vps_li.pop()

    if not vps_li:
        print('YES')
    else:
        print('NO')
