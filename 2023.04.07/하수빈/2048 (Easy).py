import sys
from copy import deepcopy
input = sys.stdin.readline

def dfs(n, b):
    global ans
    # 5번 이동하면 종료
    if n == 5:
        tmp = 0
        for i in range(N):
            for j in range(N):
                tmp = max(tmp, b[i][j])
        # tmp값이 ans보다 크다면 교체
        ans = max(ans, tmp)
        return
    
    # 4방향 이동 탐색
    dfs(n + 1, move_R(b))
    dfs(n + 1, move_L(b))
    dfs(n + 1, move_D(b))
    dfs(n + 1, move_U(b))


# 오른쪽 이동 함수
def move_R(b):
    # 들어온 board 복사
    nb = deepcopy(b)
    # 합쳐진 블록 위치 기억 배열
    comb = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N - 2, -1, -1):
            # 블록이 있다면 이동할 수 있는 위치 탐색
            if nb[i][j]:
                for k in range(j + 1, N):
                    # 이동하려는 위치에 있는 블록을 찾았다면
                    if nb[i][k]:
                        # 숫자가 같고 아직 합쳐지지 않았다면 합체
                        if nb[i][j] == nb[i][k] and not comb[i][k]:
                            nb[i][k] *= 2
                            nb[i][j] = 0
                            comb[i][k] = 1
                        # 이미 합쳐진 블록이거나 숫자가 다르다면
                        else:
                            # 원래 위치가 아니라면 이 블록 앞에 이동할 블록 위치
                            if k - 1 != j:
                                nb[i][k - 1] = nb[i][j]
                                nb[i][j] = 0
                        break
                # 다른 블록이 없다면 제일 오른쪽으로 이동
                else:
                    nb[i][N - 1] = nb[i][j]
                    nb[i][j] = 0
    return nb

def move_L(b):
    nb = deepcopy(b)
    comb = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(1, N):
            if nb[i][j]:
                for k in range(j - 1, -1, -1):
                    if nb[i][k]:
                        if nb[i][j] == nb[i][k] and not comb[i][k]:
                            nb[i][k] *= 2
                            nb[i][j] = 0
                            comb[i][k] = 1
                        else:
                            if k + 1 != j:
                                nb[i][k + 1] = nb[i][j]
                                nb[i][j] = 0
                        break
                else:
                    nb[i][0] = nb[i][j]
                    nb[i][j] = 0
    return nb

def move_D(b):
    nb = deepcopy(b)
    comb = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N - 2, -1, -1):
            if nb[j][i]:
                for k in range(j + 1, N):
                    if nb[k][i]:
                        if nb[j][i] == nb[k][i] and not comb[k][i]:
                            nb[k][i] *= 2
                            nb[j][i] = 0
                            comb[k][i] = 1
                        else:
                            if k - 1 != j:
                                nb[k - 1][i] = nb[j][i]
                                nb[j][i] = 0
                        break
                else:
                    nb[N - 1][i] = nb[j][i]
                    nb[j][i] = 0
    return nb

def move_U(b):
    nb = deepcopy(b)
    comb = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(1, N):
            if nb[j][i]:
                for k in range(j - 1, -1, -1):
                    if nb[k][i]:
                        if nb[j][i] == nb[k][i] and not comb[k][i]:
                            nb[k][i] *= 2
                            nb[j][i] = 0
                            comb[k][i] = 1
                        else:
                            if k + 1 != j:
                                nb[k + 1][i] = nb[j][i]
                                nb[j][i] = 0
                        break
                else:
                    nb[0][i] = nb[j][i]
                    nb[j][i] = 0
    return nb

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, board)
print(ans)