def QuadTree(data, n):
    m = n // 2                  # 나눈 길이
    if n == 1:                  # 최소 비트이면 그 값 리턴
        return data[0][0]
    countzero = 0

    for i in range(n):
        countzero += data[i].count('0')     # 행마다 '0'의 개수 카운트

    if countzero == n * n:      # 모두 0이면 0리턴
        return '0'
    elif countzero == 0:        # 모두 1이면 1리턴
        return '1'
    quad1 = list(map(lambda x: x[:m], data[:m]))    # 4등분을 lambda와 map을 이용해 슬라이싱
    quad2 = list(map(lambda x: x[m:], data[:m]))
    quad3 = list(map(lambda x: x[:m], data[m:]))
    quad4 = list(map(lambda x: x[m:], data[m:]))
    return '(' + QuadTree(quad1, m) + QuadTree(quad2, m) + QuadTree(quad3, m) + QuadTree(quad4, m) + ')'
    # 같은 사각형의 안의 정보를 괄호로 묶어서 리턴


N = int(input())

data_input = [list(input()) for _ in range(N)]

ans = QuadTree(data_input, N)

print(ans)
