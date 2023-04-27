import sys
sys.setrecursionlimit(100000)

def tree(start, end, index):
    # 리프노드가 곧 높이
    if start == end:
        segment_tree[index] = start
        return segment_tree[index]
    
    mid = (start + end) // 2
    # 가장 작은 높이의 위치를 찾는다.
    left = tree(start,mid,2*index)
    right = tree(mid+1, end, 2*index+1)
    segment_tree[index] = left if lst[left] <= lst[right] else right
    return segment_tree[index]

def find(start, end, index, left, right):
	# 찾으려는 범위가 start~end 범위보다 클 경우
    if start > right or end < left:
        return 0

    # 찾으려는 범위내에 최소의 높이를 구한다.
    if start >= left and end <= right:
        return segment_tree[index]

    # 현재 노드는 왼쪽아래 + 오른쪽아래 노드이다.
    mid = (start + end) // 2
    left_col = find(start, mid, index*2, left, right)
    right_col = find(mid+1, end, index*2+1, left, right)

    # 높이의 정보를 찾아온다.
    if left_col == 0:
        rlt = right_col
    elif right_col == 0:
        rlt = left_col
    else:
        rlt = left_col if lst[left_col] <= lst[right_col] else right_col
    
    return rlt 

def solv(start, end): # 넓이의 정보를 계싼한다.
    col= find(1, N, 1, start, end) # 타겟이 되는 높이가 위치한 idx 탐색
    A = (end - start + 1) * lst[col] # 넓이 계산
    
    if col + 1 <= end:
        tmp = solv(col + 1, end)
        A = max(tmp, A)
    if col - 1 >= start:
        tmp = solv(start, col - 1)
        A = max(tmp, A)

    return A

while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break
    
    N = lst[0]
    lst = [0]+lst[1:]
    segment_tree = [0]*(4*N)
    tree(1,N,1)
    print(solv(1, N))



# while True:
#     lst = list(map(int,input().split()))
#     if lst[0] == 0:
#         break
    
#     N = lst[0]
        
#     stack = []
#     max_rlt = 0
    
#     for i in range(1, N+1):
#         height = lst[i]
#         if stack and stack[-1][1] > height:
#             while stack:  # 스택에서 빼내며 최대 직사각형 넓이를 계산
#                 stack_i, stack_height = stack.pop()
#                 width_start = 1
#                 if stack:
#                     width_start = stack[-1][0]+1
#                 result = (i - width_start) * stack_height
#                 max_rlt = max(result, max_rlt) # 최대값 갱신
#                 # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산
#                 if not stack or stack[-1][1] <= height:
#                     break
#         # 스택이 비어 있거나 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 크거나 같으면
#         if not stack or stack[-1][1] <= height:
#             stack.append((i, height))  # 스택에 현재 막대기를 추가
            
#     # 반복이 종료되고, 스택에 남은 막대기가 있다면 계산
#     while stack:
#         stack_i, stack_height = stack.pop()
#         width_start = 1
#         if stack:
#             width_start = stack[-1][0]+1
#         result = (lst[0]+1 - width_start) * stack_height
#         max_rlt = max(result, max_rlt) # 최대값 갱신  
        
#     print(max_rlt)
