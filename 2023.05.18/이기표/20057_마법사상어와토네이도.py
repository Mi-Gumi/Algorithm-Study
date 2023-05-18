def rotate(sand):
    return list(reversed(list(zip(*sand))))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

si, sj = N//2, N//2
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

sand1 = [[0, 0, 0.02, 0, 0],
      [0, 0.1, 0.07, 0.01, 0],
      [0.05, 0, 0, 0, 0],
      [0, 0.1, 0.07, 0.01, 0],
      [0, 0, 0.02, 0, 0]]
sand2 = rotate(sand1)
sand3 = rotate(sand2)
sand4 = rotate(sand3)
sands = [sand1, sand2, sand3, sand4]

idx = 0
ans = 0
n = 2
while 1:
    flag = 0
    for _ in range(2):
        for __ in range(1, n):
            si += dir[idx][0]
            sj += dir[idx][1]
            if 0 <= si < N and 0 <= sj < N:
                all = arr[si][sj]
                for i in range(5):
                    for j in range(5):
                        cur = int(arr[si][sj] * sands[idx][i][j])
                        all -= cur # 전체에서 현재 빼기

                        if 0 <= si - 2 + i < N and 0 <= sj - 2 + j < N:
                            arr[si-2+i][sj-2+j] += cur
                        else: # 밖으로 나간 모래
                            ans += cur
                arr[si][sj] = 0
                if 0 <= si + dir[idx][0] < N and 0 <= sj + dir[idx][1] < N:
                    arr[si + dir[idx][0]][sj + dir[idx][1]] += all
                else:
                    ans += all

            if si < 0 or sj < 0 or si >= N or sj >= N:
                flag = True
                break

        idx = (idx + 1) % 4
    n += 1
    if flag:
        break
print(ans)