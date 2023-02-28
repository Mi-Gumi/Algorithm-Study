def inorder(v):
    if v != 0:
        
        print(v, end=' ')
        inorder(tree[v][0])
        inorder(tree[v][1])

N = int(input())
E = N - 1
tree = [[0]*3 for _ in range(N+1)]
visited = [0] * (N + 1)


for i in range(E):
    
    p, c = map(int,input().split()) # 부모, 자식.

    if tree[p][0] == 0: # 왼쪽 자식이 없으면
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p

inorder(1); print()


