def pre(node):
  if node == '.':return
  
  print(node,end='')
  pre(tree[node][0])
  pre(tree[node][1])

def mid(node):
  if node == '.':return
  
  mid(tree[node][0])
  print(node,end='')
  mid(tree[node][1])

def post(node):
  
  if node == '.':return
  
  post(tree[node][0])
  post(tree[node][1])
  print(node,end='')


T = int(input())

tree = dict()

for _ in range(T):
  parent, left, right = map(str, input().split())
  child = [left, right]
  
  tree[parent] = child


pre('A')
print()
mid('A')
print()
post('A')