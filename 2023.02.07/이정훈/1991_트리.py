class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def addchild(self, left, right):
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):  # 트리 생성
        self.root = None

    def setroot(self, n):
        self.root = n

    def preorder(self, n):
        if n:
            print(n.item, end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        if n:
            if n.left:
                self.inorder(n.left)
            print(n.item, end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        if n:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(n.item, end='')


N = int(input())

arr = [input().split() for _ in range(N)]

node_index = []
nodes = []

for i in range(N):
    node = Node(arr[i][0])
    nodes.append(node)
    node_index.append(arr[i][0])
node_index.append('.')
nodes.append(None)
for i in range(N):
    nodes[i].addchild(nodes[node_index.index(arr[i][1])], nodes[node_index.index(arr[i][2])])

Tree = BinaryTree()
Tree.setroot(nodes[node_index.index('A')])
Tree.preorder(Tree.root)
print()
Tree.inorder(Tree.root)
print()
Tree.postorder(Tree.root)
