import sys
sys.setrecursionlimit(10 ** 9)


def cut(start_y, start_x, paper_size):

    global ill, young, m_ill

    for row in range(start_y, start_y + paper_size):
        for col in range(start_x, start_x + paper_size):

            # 잘라낸 종이 안에 시작점과 다른 숫자가 있으면 그 종이를 다시 9장으로 나눠 탐색
            if paper[start_y][start_x] != paper[row][col]:
                for divided_row in range(3):
                    for divided_col in range(3):
                        cut((start_y + paper_size // 3 * divided_row), (start_x + paper_size // 3 * divided_col), (paper_size // 3))

                return

    # 시작점과 다른 부분의 숫자가 같으면 재귀가 종료되니 시작점의 숫자만 보고 갯수 파악 가능
    if paper[start_y][start_x] == 1:
        ill += 1

    if paper[start_y][start_x] == 0:
        young += 1

    if paper[start_y][start_x] == -1:
        m_ill += 1


paper_size = int(input())

paper = [list(map(int, input().split())) for _ in range(paper_size)]

ill = young = m_ill = 0

cut(0, 0, paper_size)

print(m_ill)
print(young)
print(ill)
