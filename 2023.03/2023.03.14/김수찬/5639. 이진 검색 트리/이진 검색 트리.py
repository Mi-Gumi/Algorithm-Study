import sys
sys.setrecursionlimit(10**9)

nodes = sys.stdin.readlines()
nodes = [int(node.rstrip('\n')) for node in nodes]
def left_right(s,e):
    idx = e+1 # 오른쪽 노드가 없을 경우 
    for i in range(s+1, e+1): # left 부터 end 끝까지
        if nodes[s] < nodes[i]:
            idx = i
            break
    return idx

def post(start,end):
    if start > end:
        return
    mid = left_right(start,end)
    post(start+1,mid - 1)
    post(mid,end)
    print(nodes[start])
post(0,len(nodes)-1)