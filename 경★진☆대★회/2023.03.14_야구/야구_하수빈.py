import sys
input = sys.stdin.readline
from itertools import permutations

def game(l):
    now = 0
    result = 0
    for i in range(N):
        count = 0
        ru1, ru2, ru3 = 0, 0, 0
        while count != 3:
            if score[i][l[now]] == 0:
                count += 1    
            elif score[i][l[now]] == 1:
                result += ru3
                ru1, ru2, ru3 = 1, ru1, ru2
            elif score[i][l[now]] == 2:
                result += ru2 + ru3
                ru1, ru2, ru3 = 0, 1, ru1
            elif score[i][l[now]] == 3:
                result += ru1 + ru2 + ru3
                ru1, ru2, ru3 = 0, 0, 1
            elif score[i][l[now]] == 4:
                result += ru1 + ru2 + ru3 + 1
                ru1, ru2, ru3 = 0, 0, 0
            now = (now + 1) % 9
    return result

N = int(input())
score = [list(map(int, input().split())) for  _ in range(N)]
taja = list(range(1, 9))
ans = 0

for _list in permutations(taja):
    t = list(_list[:3]) + [0] + list(_list[3:])
    tmp = game(t)
    ans = max(ans, tmp)

print(ans)