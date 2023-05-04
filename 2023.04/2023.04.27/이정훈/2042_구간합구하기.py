import sys; input = sys.stdin.readline

def build(node, left, right) :
    if left == right :
        st[node] = arr[left]
        return st[node]
    
    mid = (left + right) // 2
    st[node] = build(2*node, left, mid) + build(2*node+1, mid+1, right)
    return st[node]

def query(node, left, right, i, j) :
    #  범위를 벗어나면 0 반환
    if i > right or j < left :
        return 0
    
    # 범위가 완전히 포함 되면 해당 노드가 나타내는 구간의 값을 반환
    if i <= left and right <= j :
        return st[node]
    
    mid = (left+right) // 2
    left_sum = query(2*node, left, mid, i, j)
    right_sum = query(2*node+1, mid+1, right, i, j)
    return left_sum + right_sum

def update(node, left, right, i, j, k) :
    if i > right or j < left :
        return 0
    
    if i <= left and right <= j :
        st[node] = k

    else :
        mid = (left + right) // 2
        update(2*node, left, mid, i, j, k)
        update(2*node+1, mid+1, right, i, j, k)
        st[node] = st[2*node] + st[2*node+1]


# 미완성 코드

n, m, k = map(int,input().split())

arr = [int(input()) for _ in range(n)]
st = [0]*(n*4)

requests = [list(map(int,input().split())) for _ in range(m+k)]

build(1, 0, n-1)
# print(st)
for request in requests :
    commend, b, c = request
    if commend == 1 :
        update(1, 0 , n-1, b-1, b-1, c)
        # print(st)

    else :
        print(query(1, 0, n-1, b-1, c-1))
        # print(st)
