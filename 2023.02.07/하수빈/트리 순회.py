import sys
input = sys.stdin.readline


# 전위 순회
def preorder(tree, root):

    # root가 '.'이 아니라면
    if root != '.':

        # 각 노드에 대해 root -> 왼쪽 -> 오른쪽 순으로 출력
        print(root, end='')
        preorder(tree, tree[root][0])
        preorder(tree, tree[root][1])
    return


# 중위 순회
def inorder(tree, root):
    if root != '.':

        # 각 노드에 대해 
        inorder(tree, tree[root][0])
        print(root, end='')
        inorder(tree, tree[root][1])
    return

# 후위 순회
def postorder(tree, root):
    if root != '.':
        postorder(tree, tree[root][0])
        postorder(tree, tree[root][1])
        print(root, end='')
    return


N = int(input())
tree = {}

for _ in range(N):
    item, left, right = input().split()
    tree[item] = [left, right]

preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A'회
print()