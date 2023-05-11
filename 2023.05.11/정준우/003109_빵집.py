from sys import stdin


def steal(row, col):

    global success, pipeline

    # 열의 범위는 건물에 막혀서 중단되거나 범위를 벗어나기 전 성공으로 취급되어 종료되니, 행의 범위 이탈만 고려
    if row == -1 or row == row_size:
        return

    # 건물에 막히면 중단
    if grid[row][col] == 'x':
        return

    # 이미 연결된 파이프는 건물과 같이 다른 파이프를 막으니 동일하게 취급 가능
    grid[row][col] = 'x'

    # 성공한 경우
    if col == col_size - 1:
        success = True
        pipeline += 1
        return

    # 놓을 수 있는 파이프 모두 고려하며, 이미 해당 파이프라인이 연결 성공된 상태라면 남은 경우들 바로 중단
    for y, x in check:
        steal(row + y, col + x)
        if success:
            return


row_size, col_size = map(int, stdin.readline().split())

grid = [list(stdin.readline()) for _ in range(row_size)]

pipeline = 0

# 위쪽이 비어있다면 되도록 채워주는게 가장 많이 연결할 수 있는 방법이니, 위쪽부터 탐색해보도록 순서 조정
check = ((-1, 1), (0, 1), (1, 1))

for row in range(row_size):
    success = False
    steal(row, 0)

print(pipeline)
