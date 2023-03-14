import sys
sys.setrecursionlimit(10**9)

preorder = []
while 1:
    try:
        data = int(input())
        preorder.append(data)
    except:
        break

def trees(preorder, s, e):
    if s == e:
        return []
    # if e <= s:
    #     return [preorder[s]]

    root = preorder[s]
    idx = e
    for i in range(s+1, e):
        if preorder[i] > root:
            idx = i
            break

    tree = trees(preorder, s+1, idx) + trees(preorder, idx, e) + [preorder[s]]
    return tree
result = trees(preorder, 0, len(preorder))
# print(result)
for i in result:
    print(i)
