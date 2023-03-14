import sys
input = sys.stdin.readline

class Node: # 이진 탐색 노드 클래스 생성
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self): # 생성 트리 확인
        return f'{self.data}, {self.left_node}, {self.right_node}'

def pre_order(node): # 전위 순회
    print(node.data, end = '')
    if node.left_node != None:  # 왼쪽 노드 먼저 탐색
        pre_order(tree[node.left_node])
    if node.right_node != None: # 왼쪽 노드 탐색 후에 오른쪽 노드 탐색
        pre_order(tree[node.right_node])

def in_order(node): # 중위 순회
    if node.left_node != None:  # 왼쪽 노드 먼저 탐색
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None: # 왼쪽 노드 탐색 후에 오른쪽 노드 탐색
        in_order(tree[node.right_node])

def post_order(node): # 후위 순회
    if node.left_node != None:  # 왼쪽 노드 먼저 탐색
        post_order(tree[node.left_node])
    if node.right_node != None: # 왼쪽 노드 탐색 후에 오른쪽 노드 탐색
        post_order(tree[node.right_node])
    print(node.data, end='')

N = int(input()) # 트리의 크기
tree = {}

for _ in range(N):
    data, left_node, right_node = input().split()
    if left_node == '.':
        left_node = None
    if right_node == '.':
        right_node = None
    tree[data] = Node(data, left_node, right_node)

# for v in tree.values():
#     print(v)
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])





