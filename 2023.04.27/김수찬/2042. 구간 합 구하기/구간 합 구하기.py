import math 

N, M, K = map(int,input().split())

lst = [0] + [int(input()) for _ in range(N)]
segment_tree = [0]*(4*N) # 세그먼트 트리에 필요한 노드의 개수는 최악의 경우 리프 노드 N개 모두 탐색을 진행해야한다.
# 각각의 값은 segment_tree에서의 리프노드 들이며, 이 경우 모든 탐색을 하는 경우가 2N - 1 번을 탐색을 해야한다. (idx 를 편의상 1부터 계산한다 하면, 2N개)가 된다.
# 세그먼트 트리의 경우 일반적으로 perfect binary tree 형태를 바탕으로 노드를 만들게 되는데, 
# k 번째 노드를 탐색을 하기 위해서는 탐색되는 노드의 수는 총 2 * 2^k 개가 필요하며, 
# 2*2^k 개가 나온다. 이 때, 2^k의 범위는 M<= < 2M 이며, 존재하는 노드는 2N 개 이기 때문에 M = 2N 이다. 따라서 우리가 임의로 4N을 러프하게 곱한다.

# 1. 세그먼트 트리 트리 만들기
def tree(start, end, index):
	# start와 end가 같다면 리프노드이다.
    if start == end:
        segment_tree[index] = lst[start]
        return segment_tree[index]
	
    # 현재 노드는 왼쪽 아래 노드와 오른쪽 아래 노드를 더한 값이다.
    mid = (start+end) // 2
    segment_tree[index] = tree(start, mid, index*2) + tree(mid+1, end, index*2+1)
    return segment_tree[index]

# 2. 트리에서 값 찾기
def find(start, end, index, left, right):
	# 찾으려는 범위가 start~end 범위보다 클 경우
    if start > right or end < left:
        return 0
        
    # 찾으려는 범위가 segment tree 노드안에 구현되어 있을 경우
    if start >= left and end <= right:
        return segment_tree[index]

    # 현재 노드는 왼쪽아래 + 오른쪽아래 노드이다.
    mid = (start + end) // 2
    # 노드의 합은 찾으려는 범위 안에 있는 segemnt tree의 노드의 합과 같다.
    rlt = find(start, mid, index*2, left, right) + find(mid+1, end, index*2+1, left, right) 
    return rlt


# 3. 트리 값 바꿔주기
def update(start, end, index, update_idx, update_data):
	# update 하려는 범위가 초과될 경우// (start,end) 범위에 없을 경우
    if start > update_idx or end < update_idx:
        return
    
    segment_tree[index] += update_data
    # 리프노드까지 바꿔주었으면 재귀함수를 끝낸다.
    if start == end:
        return

	# update_idx가 관여하고 있는 노드들을 찾아서 바꿔준다.
    mid = (start + end) // 2
    # 다음 노드로 찾아간다.
    update(start, mid, index*2, update_idx, update_data)
    update(mid+1, end, index*2+1, update_idx, update_data)


tree(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1:
        temp = c - lst[b] # 값의 차이를 업데이트 시켜준다.
        lst[b] = c
        update(1, N, 1, b, temp) # 업데이트를 진행  

    elif a == 2:
        print(find(1, N, 1, b, c))