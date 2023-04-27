from sys import stdin, setrecursionlimit


# 세그먼트 트리 생성
def make_segment_tree(node, start, end):

    # 리프 노드라면, 최소 높이와 인덱스 기록
    if start == end:
        segment_tree[node] = (info[start], start)
        return segment_tree[node]

    mid = (start + end) // 2

    # 자식 노드 중 작은 값을 부모 노드에 추가
    # 직사각형은 낮은 높이를 기준으로 만들어지기 때문에 범위 내에서 가장 작은 높이를 값으로 가지게 함
    segment_tree[node] = min(make_segment_tree(node * 2, start, mid), make_segment_tree(node * 2 + 1, mid + 1, end))
    return segment_tree[node]


# 설정 범위 내 최소값과 그 인덱스를 찾기 위한 함수
def find_min(node, start, end, entire_start, entire_end):
    # 완벽히 범위 안이라면 최소 높이와 인덱스 반환
    if entire_start <= start and end <= entire_end:
        return segment_tree[node]

    # 범위 밖이라면 큰 값으로 지정
    elif start > entire_end or end < entire_start:
        return 1000000001, 0

    # 범위 안에 걸쳐 있다면 나눠서 탐색
    else:
        mid = (start + end) // 2
        return min(find_min(node * 2, start, mid, entire_start, entire_end), find_min(node * 2 + 1, mid + 1, end, entire_start, entire_end))


# 지정된 구역 내 직사각형의 최대 넓이 구하는 함수
# 탐색 중인 구역 내 가장 낮은 것을 높이로 하는, 바닥에서 시작하는 직사각형의 넓이와 가장 낮은 높이를 기준으로 나눈 양 쪽에서 나올 수 있는 사각형의 넓이 비교
def area(start, end):

    if start > end:
        return 0

    min_height, min_height_index = find_min(1, 1, num_of_unit_rectangles, start, end)
    bottom_rectangle = (end - start + 1) * min_height

    return max(bottom_rectangle, area(start, min_height_index - 1), area(min_height_index + 1, end))


setrecursionlimit(10 ** 5)

while True:
    info = list(map(int, stdin.readline().strip().split()))

    if info[0] == 0:
        break

    num_of_unit_rectangles = info[0]

    # 높이가 아닌 숫자가 영향을 주지 않게 하기 위함
    info[0] = 0

    segment_tree = [0 for _ in range(num_of_unit_rectangles * 4)]

    make_segment_tree(1, 1, num_of_unit_rectangles)

    print(area(1, num_of_unit_rectangles))








# # 스택 사용
# from sys import stdin
# from collections import deque
#
#
# while True:
#     info = list(map(int, stdin.readline().strip().split()))
#
#     num_of_unit_rectangles = info.pop(0)
#
#     if num_of_unit_rectangles == 0:
#         break
#
#     stack = deque()
#
#     the_largest = 0
#
#     for idx in range(num_of_unit_rectangles):
#         while len(stack) != 0 and info[stack[-1]] > info[idx]:
#             height_idx = stack.pop()
#
#             if len(stack) == 0:
#                 width = idx
#
#             else:
#                 width = idx - stack[-1] - 1
#
#             the_largest = max(the_largest, width * info[height_idx])
#
#         stack.append(idx)
#
#     while len(stack) != 0:
#         height_idx = stack.pop()
#
#         if len(stack) == 0:
#             width = num_of_unit_rectangles
#
#         else:
#             width = num_of_unit_rectangles - stack[-1] - 1
#
#         the_largest = max(the_largest, width * info[height_idx])
#
#     print(the_largest)
