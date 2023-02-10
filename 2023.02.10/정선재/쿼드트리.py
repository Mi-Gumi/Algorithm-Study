n = int(input())


def recursive(x, y, N):
    flag = False

    for i in range(x, x + N):
        if flag:
            break

        for j in range(y, y + N):
            if graph[x][y] != graph[i][j]:
                print('(', end = '')
                recursive(x, y, N // 2)
                recursive(x, y + N // 2, N // 2)
                recursive(x + N // 2, y, N // 2)
                recursive(x + N // 2, y + N // 2, N // 2)
                print(')', end = '')
                flag = True
                break

    if not flag:
        if graph[x][y] == 0:
            print(0, end='')
        else:
            print(1, end='')


graph = []
for i in range(n):
    graph.append(list(map(int, input())))


recursive(0, 0, n)

