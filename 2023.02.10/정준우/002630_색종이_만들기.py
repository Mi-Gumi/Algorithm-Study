def paper_cut(x, y, size):
    # 자른 색종이에서의 (0, 0) 부분 색
    color = paper[x][y]

    # 자른 색종이 범위 내 모든 요소를 탐색
    for jwa_woo in range(x, x + size):
        for wee_arae in range(y, y + size):
            # 다른 색이 나오면, 4등분 후 각 사분면의 (0, 0)에 해당하는 곳에서 반복
            if color != paper[jwa_woo][wee_arae]:
                paper_cut(x, y, size // 2)
                paper_cut(x + size // 2, y, size // 2)
                paper_cut(x + size // 2, y + size // 2, size // 2)
                paper_cut(x, y + size // 2, size // 2)
                # 색종이를 나눠야할 시 반환값 없음을 안 하니 결과로 네자리수 출력됨
                return None
    # for-else문 / 색이 모두 같아 반복문이 완전히 끝났을 경우, 흰색과 파란색 중 어떤 색인지 판단 후 해당 색에 + 1
    else:
        if color == 0:
            color_count[0] += 1
        else:
            color_count[1] += 1


size = int(input())

paper = [list(map(int, input().split())) for _ in range(size)]
color_count = [0, 0]

paper_cut(0, 0, size)

print(color_count[0])
print(color_count[1])