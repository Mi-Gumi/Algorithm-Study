def dfs(depth):
    global max_

    if depth == N:  # 만약 길이 N개를 뽑았다면
        count = 0
        for j in egg:
            if j[0] <= 0:
                count += 1
        if max_ < count:  # 그 값이 저장된 최댓값보다 크다면
            max_ = count  # 그 값을 최대값으로 저장
        return

    if egg[depth][0] <= 0:  # 만약 계란이 이미 깨져있다면
        dfs(depth + 1)  # 해당 dfs를 바로 넘어간다.
    else:  # 만약 계란이 깨져있지 않다면
        flag = False  # 나머지 계란이 모두 깨져있는지 체크
        for i in range(N):  # 다른 계란들을 살피면서
            if depth != i and egg[i][0] > 0:  # 현재 계란이 아니고 깨져있지 않다면
                egg[depth][0] -= egg[i][1]  # 공격
                egg[i][0] -= egg[depth][1]  # 공격
                flag = True  # 계란이 모두 깨져있지 않기 때문에 True 바꿔준다.
                dfs(depth + 1)  # 재귀를 돈다.
                egg[depth][0] += egg[i][1]  # 빠져나왔다면 다시 복구
                egg[i][0] += egg[depth][1]  # 다시 복구
        if not flag:  # 만약 모든 계란이 깨져있다면
            dfs(depth + 1)  # 바로 dfs를 넘어간다.


max_ = 0
N = int(input())
egg = [list(map(int, input().split())) for _ in range(N)]
dfs(0)
print(max_)