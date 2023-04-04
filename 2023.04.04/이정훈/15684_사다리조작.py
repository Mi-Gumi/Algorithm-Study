from itertools import combinations
import sys
input = sys.stdin.readline

def check():
    for i in range(1, N+1):
        now = i
        for j in range(H):
            if ladders[j][now-1] == 1:
                now -= 1
            elif ladders[j][now] == 1:
                now += 1
        if now != i:
            return False
    return True


N, M, H = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)]
ladders = [[0]*(N+1) for _ in range(H)]
ans = -1

# make 사다리
for a, b in infos:
    ladders[a-1][b] = 1

# 후보자리
candidate = []
for i in range(H):
    for j in range(1, N):
        if ladders[i][j] == 0:
            for di, dj in ((0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < N+1 and ladders[ni][nj] == 1:
                    break
            else:
                candidate.append([i, j])


if check():
    ans = 0

if ans == -1:
    for cnt in range(1, 4):
        if ans != -1:
            break
        combi = list(combinations(candidate, cnt))
        for com in combi:
            for i, j in com:
                ladders[i][j] = 1

            if check():
                ans = cnt
                break

            for i, j in com:
                ladders[i][j] = 0

print(ans)
