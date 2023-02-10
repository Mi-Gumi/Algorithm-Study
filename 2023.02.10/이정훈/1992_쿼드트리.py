def QuadTree(data, n):
    m = n // 2
    if n == 1:
        return data[0][0]
    countzero = 0

    for i in range(n):
        countzero += data[i].count('0')

    if countzero == n * n:
        return '0'
    elif countzero == 0:
        return '1'
    quad1 = list(map(lambda x: x[:m], data[:m]))
    quad2 = list(map(lambda x: x[m:], data[:m]))
    quad3 = list(map(lambda x: x[:m], data[m:]))
    quad4 = list(map(lambda x: x[m:], data[m:]))
    return '(' + QuadTree(quad1, m) + QuadTree(quad2, m) + QuadTree(quad3, m) + QuadTree(quad4, m) + ')'


N = int(input())

data_input = [list(input()) for _ in range(N)]

ans = QuadTree(data_input, N)

print(ans)
