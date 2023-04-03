T = int(input())
table = [list(map(int,input().split())) for _ in range(T)]
players = [i for i in range(T)]
team = [False for _ in range(T)]

rlt = []

def solv():
    f_t = 0
    t_t = 0
    for i in range(T):
        target = 0
        for j in range(T):
            if team[i] == team[j]:
                target += table[i][j]
        if team[i]:
            t_t += target
        else:
            f_t += target
    return abs(t_t - f_t)

def bt(p, end):
    if end == team.count(False):
        vs = solv()
        if vs not in rlt:
            rlt.append(vs)
        return

    for player in range(p, len(players)):
        if team[player]:
            continue
        team[player] = True
        bt(player, end)
        team[player] = False  

bt(0, T//2)
print(min(rlt))