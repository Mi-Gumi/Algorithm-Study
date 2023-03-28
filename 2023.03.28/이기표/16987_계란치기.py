N = int(input())
egg = [list(map(int, input().split())) for _ in range(N)]
ans = 0
def recur(depth):
    global ans
    if depth == N:
        cnt = 0
        for e in egg:
            if e[0] <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return

    # 현재 depth에서 계란이 깨진 경우
    if egg[depth][0] <= 0:
        recur(depth+1)
        return

    # 깨진 계란을 탐색
    flag = 1
    for i in range(N):
        if depth != i:
            if egg[i][0] > 0:
                flag = 0

    # 깨진 계란이 있다면 
    if flag:
        cnt = 0
        for e in egg:
            if e[0] <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return
    
    # 계란 치기
    for i in range(N):
        if depth != i:
            if egg[i][0] > 0 and egg[depth][0] > 0:
                egg[i][0] -= egg[depth][1]
                egg[depth][0] -= egg[i][1]
                recur(depth+1)
                egg[i][0] += egg[depth][1]
                egg[depth][0] += egg[i][1]
recur(0)
print(ans)


