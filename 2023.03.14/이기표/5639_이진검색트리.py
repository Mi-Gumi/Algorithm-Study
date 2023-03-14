'''
전위 순회는 루트 왼쪽 오른쪽 순으로 탐색
하지만 후위 순회는 왼쪽 오른쪽 루트 순으로 탐색하기때문에
정점의 크기를 비교하여 왼쪽 오른쪽을 탐색하여 후위순회를 완성
'''
import sys
sys.setrecursionlimit(10**9)

preorder = [] # 전위 순회값
while 1:
    try:
        data = int(input())
        preorder.append(data)
    except:
        break

def trees(preorder, s, e):
    if s == e: # 모두 탐색하면 결과 반환
        return []
    # if e <= s:
    #     return [preorder[s]]
    root = preorder[s] # 루트
    idx = e # 왼쪽 오른쪽을 정하는 기준 인덱스
    for i in range(s+1, e): # 루트노드 다음값과 비교해 왼쪽노드 오른쪽 노드 판별
        if preorder[i] > root:
            idx = i
            break
    # 왼쪽 오른쪽 루트 순으로 재귀 진행후 합치기
    tree = trees(preorder, s+1, idx) + trees(preorder, idx, e) + [preorder[s]]
    return tree
result = trees(preorder, 0, len(preorder))
# print(result)
for i in result:
    print(i)
