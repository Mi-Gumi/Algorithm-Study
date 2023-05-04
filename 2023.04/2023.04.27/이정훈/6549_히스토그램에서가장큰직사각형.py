"""
히스토그램에서 가장 큰 직사각형의 넓이를 출력한다.
세그먼트 트리를 통해 구간 내의 가장 낮은 높이와 그 구간에서의 사각형 넓이를 저장한다.
"""
import sys; input = sys.stdin.readline

# def build(node, left, right) :
#     global ans
#     if left == right :
#         st[node] = (arr[left], arr[left])
#         ans = max(ans, arr[left])
#         return st[node]
    
#     mid = (left + right) // 2
#     minval = min(build(2*node, left, mid)[0] , build(2*node+1, mid+1, right)[0])
#     area = minval * (right - left + 1)
#     ans = max(ans, area)
#     st[node] = (minval , area)
#     return st[node]

while True :
    his_toe_gram = list(map(int,input().split()))
    if his_toe_gram == [0] :
        break

    n , *his_toe_gram = his_toe_gram
    st = [0]*(4*n)

    arr = his_toe_gram
    ans = 0
    # build(1, 0, n-1)
    # print(ans)

    stack = []
    for num in range(n) :
        if not stack :
            stack.append(num)
            continue
        
        while stack[-1] > num :
            popnum = stack.pop()
            # 사각형 만들어보고 값 갱신
        stack.append(num)

    while stack :
        # 나머지로 사각형 만들기
        pass

    print(ans)
