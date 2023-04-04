N, M, H = map(int, input().split())
ladder = [ [0] * (N+1) for _ in range(H+1) ]
horizon_line = [ list(map(int, input().split())) for _ in range(M) ] # 가로선의 정보
ladder_position = []
answer = 4

for a, b in horizon_line: # 가로선의 정보를 기록
    ladder[a][b] = 1

for i in range(1, H+1): # 백트래킹을 돌면서 가로선을 놓을 좌표를 기록한다. (가로선을 놓을려면 양옆으로 가로선이 없어야 놓을 수 있다.)
    for j in range(1, N):
        if ladder[i][j-1] == 0 and ladder[i][j+1] == 0 and ladder[i][j] == 0:
            ladder_position.append((i, j))

def ladder_down(): # 사다리를 내려가는 함수

    for i in range(1, N+1):
        now = i
        for j in range(1, H+1):
            if ladder[j][now] == 1: # 오른쪽으로 이동
                now += 1
            elif ladder[j][now-1] == 1: # 왼쪽으로 이동
                now -= 1

        if now != i: # i번 세로선이 i번 그대로 나오지 않으면 False를 return
            return False

    return True # i번 세로선이 i번 그대로 나온다면 True를 return

def line_arrange(depth, idx): # 가로선을 배치하는 함수
    global answer

    if ladder_down(): # 사다리를 내려가는 함수를 통해 True가 return이 되면 최소값을 갱신 (depth == 가로선을 배치한 개수)
        answer = min(answer, depth)
        return

    if depth == 3 or depth >= answer: # 만약 가로선이 4개가 넘거나 현재 최소값보다 클 경우 return
        return

    for i in range(idx, len(ladder_position)): # 미리 가로선을 놓을 수 있는 좌표를 이용해서 백트래킹
        x, y = ladder_position[i]
        if ladder[x][y-1] == 0 and ladder[x][y+1] == 0: #
            ladder[x][y] = 1
            line_arrange(depth+1, i+1)
            ladder[x][y] = 0

line_arrange(0, 0)
print(answer if answer < 4 else -1)