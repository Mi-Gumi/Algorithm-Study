N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

tetro = [ # 해당하는 테트로미노 모양(회전, 대칭 포함) 생성
    [[1, 1, 1, 1]],
    [[1], [1], [1], [1]],

    [[1, 1], [1, 1]],

    [[1, 0],
     [1, 0],
     [1, 1]],
    [[1, 1],
     [1, 0],
     [1, 0]],
    [[1, 1],
     [0, 1],
     [0, 1]],
    [[0, 1],
     [0, 1],
     [1, 1]],
    [[1, 1, 1],
     [1, 0, 0]],
    [[1, 1, 1],
     [0, 0, 1]],
    [[1, 0, 0],
     [1, 1, 1]],
    [[0, 0, 1],
     [1, 1, 1]],

    [[1, 1, 0],
     [0, 1, 1]],
    [[0, 1, 1],
     [1, 1, 0]],
    [[1, 0],
     [1, 1],
     [0, 1]],
    [[0, 1],
     [1, 1],
     [1, 0]],

    [[1, 1, 1],
     [0, 1, 0]],
    [[0, 1, 0],
     [1, 1, 1]],
    [[1, 0],
     [1, 1],
     [1, 0]],
    [[0, 1],
     [1, 1],
     [0, 1]],
]

def search(shape, x, y): # 모양에 크기에 맞춰 2차원 배열을 탐색
    max_s = 0
    for i in range(N-y+1):
        for j in range(M-x+1):
            sum_tmp = 0
            for p in range(y):
                for q in range(x):
                    # 2차원 배열의 한 칸의 요소와 테트로미노의 요소를 곱해 값을 누적
                    sum_tmp += shape[p][q] * arr[i+p][j+q]
            # 최대값 찾기
            max_s = max(max_s, sum_tmp)
    return max_s

max_sum = 0
# 19가지 모양에 해당하는 전체를 탐색
for shape in tetro:
    x = len(shape[0])
    y = len(shape)
    result = search(shape, x, y)
    # 최대값 찾기
    max_sum = max(max_sum, result)
print(max_sum)


