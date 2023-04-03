import sys
from collections import deque
input = sys.stdin.readline


def check():
    global now_dir
    ans = 0
    while True:
        dr, dc = d[now_dir]
        # 다음 위치가 게임판 안이고 현재 뱀의 몸안이 아니라면
        if 1 <= snake[-1][0] + dr <= N and 1 <= snake[-1][1] + dc <= N and [snake[-1][0] + dr, snake[-1][1] + dc] not in snake:
            # 뱀 위치 추가
            snake.append([snake[-1][0] + dr, snake[-1][1] + dc])
            # 뱀이 이동한 위치에 사과가 없다면
            if snake[-1] not in apple:
                # 뱀 꼬리 제거
                snake.popleft()
            # 사과가 있다면
            else:
                # 먹은 사과 제외
                apple.remove(snake[-1])
        # 뱀 몸이나 벽에 부딫혔다면
        else:
            # 시간 반환
            return ans + 1
        ans += 1
        # 아직 멍령어가 남아있다면
        if cmd_list:
            # 현재 시간이 명령어 시간과 같다면
            if ans == cmd_list[-1][0]:
                # L이라면 왼쪽으로 회전
                if cmd_list[-1][1] == 'L':
                    if now_dir == 0:
                        now_dir = 3
                    else:
                        now_dir -= 1
                # 아니라면 오른쪽으로 회전
                else:
                    if now_dir == 3:
                        now_dir = 0
                    else:
                        now_dir += 1
                # 사용한 명령어 제거
                cmd_list.pop()


N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
now_dir = 0
snake = deque([[1, 1]])
cmd_list = []
for _ in range(L):
    tmp, cmd = input().strip().split()
    tmp = int(tmp)
    cmd_list.append([tmp, cmd]) 
cmd_list.reverse()

print(check())
