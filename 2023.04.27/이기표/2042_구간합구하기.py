import sys
input = sys.stdin.readline

# 세그먼트 트리 만들기 (완전 이진트리 만들기)
def build(node, start, end):
    if start == end:
        # 리프 노드라면 값 저장
        tree[node] = lst[start]
        return

    mid = (start+end)//2
    # 왼쪽 자식으로 이동
    build(node * 2, start, mid)
    # 오른쪽 자식으로 이동
    build(node * 2+1, mid+1, end)
    # 왼쪽과 오른쪽 자식의 합을 부모노드에 저장
    tree[node] = tree[node*2] + tree[node*2+1]
    return

def query(node, start, end, left, right):
    # 노드가 지정된 범위 밖
    if right < start or end < left:
        return 0
    # 노드가 지정된 범위 -> 찾는 범위가 트리 노드내에 구현이 된 경우
    if left <= start and end <= right:
        return tree[node]
    # 일부의 노드만 지정된 범위 내 -> 현재 노드는 왼쪽아래 + 오른쪽 아래
    mid = (start + end) // 2
    left_child = query(node*2, start, mid, left, right)
    right_child = query(node*2+1, mid+1, end, left, right)

    return left_child + right_child

def update(node, start, end, index, val):
    if start == end:
        tree[node] = val
        return

    mid = (start + end) // 2
    # index가 포함된 구간을 가진 자식 노드로 이동
    if start <= index and index <= mid:
        update(2*node, start, mid, index, val)
    else:
        update(2*node+1, mid+1, end, index, val)
    # 왼, 오 두 자식 노드의 합을 저장
    tree[node] = tree[node*2] + tree[node*2+1]
    return

N, M, K = map(int, input().split())

lst = []
tree = [0] * (N*4)
for _ in range(N):
    n = int(input())
    lst.append(n)
# 세그먼트 트리 생성
build(1, 0, N-1)
# print(tree)
for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1: # 구간 update
        print(tree)
        update(1, 0, N-1, b-1, c)
        print(tree)
    else: # 구간합 구하기
        print(query(1, 0, N-1, b-1, c-1))
