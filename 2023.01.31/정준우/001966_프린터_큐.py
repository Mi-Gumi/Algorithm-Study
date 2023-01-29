import sys

test_cases = int(sys.stdin.readline())

for test_case in range(test_cases):
    num_of_doc, target_idx = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))

    # 인쇄 횟수를 의미하는 count 초기화
    count = 0

    # 주어진 문서의 수만큼 요소가 채워진, 목표 문서의 위치를 의미할 리스트 생성
    target_check = ['potato' for _ in range(num_of_doc)]

    # 목표 문서의 인덱스를 감자가 아닌 target 으로 구분
    target_check[target_idx] = 'target'

    while True:
        # 큐의 제일 앞에 있는 문서의 중요도가 가장 높으면, 인쇄가 이루어지니 count에 1 더하기
        if importance[0] == max(importance):
            count += 1

            # 인쇄된 문서가 목표 문서였다면, 지금까지 인쇄한 횟수를 출력하며 반복 중단
            if target_check[0] == 'target':
                print(count)
                break
            # 인쇄된 문서가 목표 문서가 아니었다면, 해당 문서와 연결된 요소들 모두 제거
            else:
                del target_check[0]
                del importance[0]

        # 큐의 제일 앞에 있는 문서의 중요도가 가장 높지 않다면, 그 문서와 연결된 요소들 모두 제거 및 반환 후 다시 리스트의 제일 뒤로 추가
        else:
            target_check.append(target_check.pop(0))
            importance.append(importance.pop(0))