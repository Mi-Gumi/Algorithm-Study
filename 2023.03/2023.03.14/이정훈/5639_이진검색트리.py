import sys
sys.setrecursionlimit(1<<15)
input = sys.stdin.readline

def postorder(left, right) :
    if left > right :
        return
    center = right + 1
    for i in range(left + 1, right+1) :
        if preorder[i] > preorder[left] :
            center = i
            break
    postorder(left + 1, center-1)
    postorder(center, right)
    ans.append(preorder[left])
    
preorder = list()
while True :
    try : 
        preorder.append(int(input()))
    except :
        break
    
ans = []
postorder(0, len(preorder)-1)

print(*ans, sep='\n')