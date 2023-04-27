import sys
input = sys.stdin.readline


def segment(node, left, right):
    # 리프 노드라면
    if left == right:
        # 자신의 값 저장
        tree[node] = arr[left]
    else:
        mid = (left + right) // 2
        # 자신 왼쪽 트리와 오른쪽 트리의 합 저장
        tree[node] = segment(node * 2, left, mid) + segment(node * 2 + 1, mid + 1, right)
    
    return tree[node]


def change(node, left, right, target, num):
    # 트리에 타겟이 없다면 종료
    if left > target or right < target:
        return
    
    # 트리 합산값 변환
    tree[node] += num

    if left != right:
        # 자식 노드 탐색
        mid = (left + right) // 2
        change(node * 2, left, mid, target, num)
        change(node * 2 + 1, mid + 1, right, target, num)


def _sum(node, left, right, start, end):
    # 트리와 구간이 겹치지 않는다면 종료
    if left > end or right < start:
        return 0
    
    # 구간안에 트리가 완전히 포함된다면 트리값 반환
    if left >= start and right <= end:
        return tree[node]

    # 자식 노드 탐색
    mid = (left + right) // 2
    return _sum(node * 2, left, mid, start, end) + _sum(node * 2 + 1, mid + 1, right, start, end)


N, M, K = map(int, input().split())

arr = [0]
tree = [0] * 4000000
for _ in range(N):
    arr.append(int(input()))

segment(1, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        # 바꿔야 하는 값
        value = c - arr[b]
        arr[b] = c
        change(1, 1, N, b, value)
    else:
        print(_sum(1, 1, N, b, c))
