import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline


def segment(node, s, e):
    # 리프 노드라면
    if s == e:
        # 자신의 인덱스 저장
        tree[node] = s
        return s

    m = (s + e) // 2
    # 좌측 노드의 높이 최솟값이 더 작다면 좌측 노드의 값 저장 아니라면 우측 노드의 값 저장
    tree[node] = tree[node * 2] if arr[segment(node * 2, s, m)] <= arr[segment(node * 2 + 1, m + 1, e)] else tree[node * 2 + 1]
    return tree[node]


# 구간 에서의 최솟값 탐색
def _min(node, l, r, s, e):
    # 트리가 구간 밖이라면 -1 반환
    if l > e or r < s: return -1
    
    # 트리가 구간 안이라면 트리의 값 반환
    if l >= s and r <= e: return tree[node]
    
    # 트리와 구간이 겹쳐있다면
    m = (l + r) // 2
    # 왼쪽 노드의 최솟값
    left_min = _min(node * 2, l, m, s, e)
    # 오른쪽 노드의 최솟값
    right_min = _min(node * 2 + 1, m + 1, r, s, e)
    # 왼쪽이 -1이라면 오른쪽
    if left_min == -1: return right_min
    # 오른쪽이 -1이라면 왼쪽
    if right_min == -1: return left_min
    # 작은 높이 인덱스 반환
    return left_min if arr[left_min] <= arr[right_min] else right_min


# 넓이 최댓값 탐색
def _max(s, e):
    global ans
    # 구간의 최솟값 탐색
    min_index = _min(1, 0, N - 1, s, e)
    # 원래 ans값과 새로운 넓이 값중 최대값으로 ans 교체
    ans = max(ans, arr[min_index] * (e - s + 1))

    # min_index구간이 남아 있다면 최솟값이 min_index가 되기 때문에 제외하고 양쪽 구간 탐색
    # min_index에서 1을 뺄 수 있다면 왼쪽 구간 탐색
    if s < min_index: _max(s, min_index - 1)
    # min_index에서 1을 더할 수 있다면 오른쪽 구간 탐색
    if e > min_index: _max(min_index + 1, e)


while True:
    arr = [*map(int, input().split())]
    if not arr[0]:
        break
    N = arr[0]
    arr = arr[1:]
    tree = [0] * (N * 4)
    segment(1, 0, N - 1)
    ans = 0
    _max(0, N - 1)
    print(ans)