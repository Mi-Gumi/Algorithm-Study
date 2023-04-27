import sys
input = sys.stdin.readline


# -를 기준으로 문자열 분리
_list = input().strip().split('-')
ans = 0
i = 0
tmp = []
# +를 기준으로 첫번째 요소만 모두 더하고 나머지는 빼기
while i < len(_list[0]):
    if _list[0][i] == '+':
        ans += int(''.join(tmp))
        tmp = []
    else:
        tmp.append(_list[0][i])
    i += 1
ans += int(''.join(tmp))

tmp = []
for i in range(1, len(_list)):
    j = 0
    while j < len(_list[i]):
        if _list[i][j] == '+':
            ans -= int(''.join(tmp))
            tmp = []
        else:
            tmp.append(_list[i][j])
        j += 1
    ans -= int(''.join(tmp))
    tmp = []

print(ans)