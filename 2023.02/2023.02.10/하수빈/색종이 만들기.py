import sys
input = sys.stdin.readline

# 종이를 나누는 함수 흰 종이와 파란 종이 갯수를 기본적으로 0으로 설정
def divide(paper, count_w=0, count_b=0):
    # 1의 갯수 선언
    count_1 = 0
    # 0의 갯수 선언
    count_0 = 0

    # paper안에 0의 갯수와 1의 갯수 탐색
    for lst in paper:
        for num in lst:
            if num == 1:
                count_1 += 1
            else:
                count_0 += 1

    # 1의 갯수가 종이의 넓이와 같다면 완전 파란 종이 임으로
    if count_1 == len(paper) ** 2:
        # 파란 종이 갯수 + 1
        count_b += 1
    # 0의 갯수가 종이의 넓이와 같다면 완전 흰 종이 임으로
    elif count_0 == len(paper) ** 2:
        # 흰 종이 갯수 + 1
        count_w += 1
    # 1, 0이 섞여있다면
    else:
        # 종이를 4부분으로 나눌 리스트 선언
        paper_1 = []
        paper_2 = []
        paper_3 = []
        paper_4 = []
        # 종이를 가로 중앙선 세로 중앙선을 기준으로 분해
        for i in range(len(paper) // 2):
            paper_1.append(paper[i][:len(paper) // 2])
            paper_2.append(paper[i][len(paper) // 2:])
            paper_3.append(paper[i + len(paper) // 2][:len(paper) // 2])
            paper_4.append(paper[i + len(paper) // 2][len(paper) // 2:])
        # 나눈 종이를 다시 divide한 결과를 담을 tmp리스트 선언
        tmp = []
        # 나눈 종이들을 divide하고 tmp에 저장
        tmp.append(divide(paper_1, count_w, count_b))
        tmp.append(divide(paper_2, count_w, count_b))
        tmp.append(divide(paper_3, count_w, count_b))
        tmp.append(divide(paper_4, count_w, count_b))
        # 결과들로 나온 흰 종이와 파란 종이의 갯수를 원래 흰 종이와 파란 종이의 갯수에 추가
        for i in range(4):
            count_w += tmp[i][0]
            count_b += tmp[i][1]
        # 결과를 튜플로 반환
    return count_w, count_b


N = int(input())
# 종이 생성
paper = [list(map(int, input().split())) for _ in range(N)]
# divide 함수 사용
c_w, c_b = divide(paper)
# 결과 출력
print(c_w)
print(c_b)