import sys
input = sys.stdin.readline


# 전위 순회
def preorder(tree, root):

    # root가 '.'이 아니라면
    if root != '.':

        # 각 노드에 대해 root를 출력하고 왼쪽 -> 오른쪽 순으로 다시 전위순회
        print(root, end='')
        preorder(tree, tree[root][0])
        preorder(tree, tree[root][1])
    return


# 중위 순회
def inorder(tree, root):
    if root != '.':

        # 각 노드에 대해 왼쪽을 중위 순회 한 후 root를 출력하고 오른쪽을 다시 중위순회
        inorder(tree, tree[root][0])
        print(root, end='')
        inorder(tree, tree[root][1])
    return

# 후위 순회
def postorder(tree, root):
    if root != '.':

        # 각 노드에 대해 왼쪽 -> 오른쪽 순서로 후위순회 한 후 root를 출력
        postorder(tree, tree[root][0])
        postorder(tree, tree[root][1])
        print(root, end='')
    return


N = int(input())

# 딕셔너리 형태로 트리 선언
tree = {}

# item을 키로 갖는 값에 left와 right로 이루어진 배열을 추가
for _ in range(N):
    item, left, right = input().split()
    tree[item] = [left, right]

# 전위순회
preorder(tree, 'A')
print()
# 중위순회
inorder(tree, 'A')
print()
<<<<<<< HEAD
postorder(tree, 'A'회
=======
# 후위순회
postorder(tree, 'A')
>>>>>>> 6071831abec71f112f94c09cdb8e88f568d2dd3b
print()