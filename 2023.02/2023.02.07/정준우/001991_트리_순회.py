# 트리를 다룰 빈 딕셔너리 생성
tree = {}

N = int(input())

# 부모 노드를 key, 자식 노드를 value에
# 인덱스를 통해 value에 접근 가능
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]


# 전위 순회  (루트 -> 왼쪽 -> 오른쪽)
# 첫 줄 아래에 탐색 멈출 부분을 위해 root가 아닌 조건 부여
def preorder(root):
    if root != '.':
        print(root, end = '')
        # left 값을 다시 새로운 root로 지정해 반복
        preorder(tree[root][0])
        # right 값을 다시 새로운 root로 지정해 반복
        preorder(tree[root][1])


# 중위 순회  (왼쪽 -> 루트 -> 오른쪽)
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end = '')
        inorder(tree[root][1])


# 후위 순회  (왼쪽 -> 오른쪽 -> 루트)
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = '')

preorder('A')
print('')
inorder('A')
print('')
postorder('A')
