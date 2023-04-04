import sys
input = sys.stdin.readline

def recur(k) :
    global min_cost, select_ans
    
    if temp_nutrition[4] >= min_cost :
        return
    if temp_nutrition[0] >= mdan and temp_nutrition[1] >= mji and temp_nutrition[2] >= mtan and temp_nutrition[3] >= mvita :
        if min_cost > temp_nutrition[4] :
            min_cost = temp_nutrition[4]
            select_ans = [temp_nutrition[4]] + select
        return
    for i in range(k, N+1) :
        select.append(i)
        for j in range(5) :
            temp_nutrition[j] += food[i][j]
        recur(i+1)
        for j in range(5) :
            temp_nutrition[j] -= food[i][j]
        select.pop()
N = int(input())
mdan, mji, mtan, mvita = map(int,input().split()) 

food = [list(map(int,input().split())) for _ in range(N)]
food = [[0]*5] + food

min_cost = 2000000
select = []

temp_nutrition = [0,0,0,0,0]
select_ans = []

recur(1)

if select_ans:
    print(select_ans[0])
    print(*select_ans[1:])
else :
    print(-1)
