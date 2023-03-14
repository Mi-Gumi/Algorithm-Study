import sys
sys.setrecursionlimit(10 ** 9)


def postorder(values):
    # if not values:
    #     return

    # 재귀 결과로 요소가 하나만 있으면 출력
    if len(values) == 1:
        print(*values)
        return

    # [98, 52, 60] 을 살펴볼 때 아래 조건문과 합쳐져 98의 오른쪽 자식으로 60이 들어가지 않게 하기 위함
    right_node_idx = len(values)

    # 루트보다 큰 값 찾기
    for idx in range(1, len(values)):
        if values[idx] > values[0]:
            right_node_idx = idx
            break

    # 왼쪽 트리
    if right_node_idx > 1:
        postorder(values[1 : right_node_idx])

    # 오른쪽 트리
    if right_node_idx < len(values):
        postorder(values[right_node_idx : ])

    # 루트 노드 출력
    print(values[0])


values = []

# 입력값 받기
while True:
    try:
        value = int(input())
        values.append(value)
    except:
        break

postorder(values)
