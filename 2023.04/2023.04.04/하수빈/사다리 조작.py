import sys
input = sys.stdin.readline

def move(n):
    global ans
    # 사다리의 각 출발 위치에 대해서 사다리 끝까지 탐색
    for o in range(N):
        i = 0
        j = o
        flag = 0
        while i != H:
            # 직전에 아래로 내려왔다면 좌우탐색
            if not flag and ladder[i][j]:
                flag = 1
                # 1이라면 오른쪽으로 이동
                if ladder[i][j] == 1:
                    j += 1
                # 2라면 왼쪽으로 이동
                else:
                    j -= 1
            else:
                flag = 0
                i += 1
        if j != o:
            return
    ans = n

def check(n, s):
    # ans보다 n이 크다면 종료
    if n >= ans:
        return
    
    move(n)

    # n이 3이면 종료
    if n == 3:
        return

    for i in range(s, H * (N - 1)):
        # H * (N - 1)개 만큼의 조합 생성
        r = i // (N - 1)
        c = i % (N - 1)
        if not ladder[r][c] and not ladder[r][c + 1]:
            ladder[r][c] = 1
            ladder[r][c + 1] = 2
            check(n + 1, i)
            ladder[r][c] = ladder[r][c + 1] = 0


N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]
ans = 10 ** 9
for _ in range(M):
    # 사다리의 왼쪽 부분을 1로 오른쪽 부분을 2로 지정
    a, b = map(int, input().split())
    ladder[a - 1][b - 1] = 1
    ladder[a - 1][b] = 2
check(0, 0)
if ans == 10 ** 9:
    print(-1)
else:
    print(ans)