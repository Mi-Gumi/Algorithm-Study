def pt(tree, root):
    if root != '.':
        print(root, end = '')
        pt(tree, tree[root][0])
        pt(tree, tree[root][1])
    
def it(tree, root):
    if root != '.':
        it(tree, tree[root][0])
        print(root, end = '')
        it(tree, tree[root][1])

def bpt(tree, root):
    if root != '.':
       bpt(tree, tree[root][0])
       bpt(tree, tree[root][1])
       print(root, end = '')

N = int(input())
tree = {}

for i in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]


pt(tree, 'A')
print()
it(tree, 'A')
print()
bpt(tree, 'A')
