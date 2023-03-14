import sys
input = sys.stdin.readline

# 쿼드 트리 함수
def quad_tree(image, ans):

    # 1과 0의 갯수를 담을 변수 선언
    count_1 = 0
    count_0 = 0

    # image 안의 1과 0의 갯수를 저장
    for lst in image:
        for num in lst:
            if num == '1':
                count_1 += 1
            else:
                count_0 += 1

    # image의 넓이와 1의 갯수가 같다면
    if count_1 == len(image) ** 2:
        # 정답 문자열에 1추가
        ans += '1'
    # image의 넓이와 0의 갯수가 같다면
    elif count_0 == len(image) ** 2:
        # 정답 문자열에 0추가
        ans += '0'
    # 1, 0이 섞여있다면
    else:
        # 정답 문자열에 여는 괄호 추가
        ans += '('
        # image를 4부분으로 나눌 리스트 선언
        image_1 = []
        image_2 = []
        image_3 = []
        image_4 = []
        # image를 가로 중앙선 세로 중앙선을 기준으로 분해
        for i in range(len(image) // 2):
            image_1.append(image[i][:len(image) // 2])
            image_2.append(image[i][len(image) // 2:])
            image_3.append(image[i + len(image) // 2][:len(image) // 2])
            image_4.append(image[i + len(image) // 2][len(image) // 2:])

        # 나눈 image를 다시 순서대로 quad_tree한 결과를 정답 문자열에 저장
        ans = quad_tree(image_1, ans)
        ans = quad_tree(image_2, ans)
        ans = quad_tree(image_3, ans)
        ans = quad_tree(image_4, ans)
        # 정답 문자열에 닫는 괄호 추가
        ans += ')'

    # 정답 문자열 반환
    return ans


N = int(input())
# image 생성
image = [list(input())[:-1] for _ in range(N)]
# 정답 문자열 선언
ans = ''
# quad_tree 실행
ans = quad_tree(image, ans)
# 정답 문자열 출력
print(ans)
