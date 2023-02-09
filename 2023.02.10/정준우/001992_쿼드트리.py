def quad_tree(x, y, size):
    # 잘라낸 영상에서의 (0, 0) 부분 점 색
    color = pixels[x][y]

    # 자른 영상 범위 내 모든 요소를 탐색
    for jwa_woo in range(x, x + size):
        for wee_arae in range(y, y + size):
            # 다른 색이 나오면, 4등분 후 각 사분면의 (0, 0)에 해당하는 곳에서 반복
            if color != pixels[jwa_woo][wee_arae]:
                # 영상을 나눌 때 괄호 안에 들어가도록
                # 함수 순서 주의
                result.append('(')
                quad_tree(x, y, size // 2)
                quad_tree(x, y + size // 2, size // 2)
                quad_tree(x + size // 2, y, size // 2)
                quad_tree(x + size // 2, y + size // 2, size // 2)
                result.append(')')
                return None
    # for-else문 / 나눈 부분의 색이 모두 같아 반복문이 완전히 끝나며
    # 압축 가능하다면 해당 색을 결과 리스트에 추가
    else:
        if pixels[x][y]:
            result.append(1)
        else:
            result.append(0)


size = int(input())

result = []

pixels = [list(map(int, input())) for _ in range(size)]

quad_tree(0, 0, size)

print(''.join(map(str, result)))