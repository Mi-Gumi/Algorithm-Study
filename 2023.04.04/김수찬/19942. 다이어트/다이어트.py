N = int(input())
def bt(now, end, is_used):
    global ans_used, ans_money

    if energy[4] >= ans_money: # 현재 비용과 ans_money 비교
        # 비교되는 시점부터 이후기 때문에, 고려 x
        return

    if (energy[0] >= have[0]) and (energy[1] >= have[1]) and (energy[2] >= have[2]) and (energy[3] >= have[3]):
        if energy[4] < ans_money:
            ans_money = energy[4]
            ans_used = is_used[:]
        return

    if now == end:
        return

    for i in range(now,N+1):
        if is_travel[i]: continue

        is_travel[i] = True
        is_used.append(i)
        energy[0] += foods[i][0]
        energy[1] += foods[i][1]
        energy[2] += foods[i][2]
        energy[3] += foods[i][3]
        energy[4] += foods[i][4]

        bt(i, end, is_used)
    
        is_travel[i] = False
        is_used.pop()
        energy[0] -= foods[i][0]
        energy[1] -= foods[i][1]
        energy[2] -= foods[i][2]
        energy[3] -= foods[i][3]
        energy[4] -= foods[i][4]


# 단백질, 지방, 탄수화물, 비타민
have = list(map(int,input().split()))

foods = [0]+[list(map(int,input().split())) for _ in range(N)]
is_travel = [False]*(N+1)

ans_money = 500*N
ans_used = []

energy = [0, 0, 0, 0, 0]
bt(1,N+1,[])
if ans_used:
    print(ans_money)
    print(*ans_used) 
else:
    print(-1)