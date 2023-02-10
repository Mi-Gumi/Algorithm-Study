import sys
# input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
ans = []
def quad_tree(arr, x, y, n):
    zero_cnt = one_cnt = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j]: # 1을 만나면 카운트
                one_cnt += 1
            else: # 0을 만나면 카운트
                zero_cnt += 1
    if one_cnt == n**2: # 면적이 다 1로 가득 찼다면
        ans.append('1')
        return

    if zero_cnt == n**2: # 면적이 다 2로 가득 찼다면
        ans.append('0')
        return   

    # 각 사분면에 따라 나눠 주기
    ans.append(('('))
    quad_tree(arr, x, y, n//2)
    quad_tree(arr, x, y+n//2, n//2)
    quad_tree(arr, x+n//2, y, n//2)
    quad_tree(arr, x+n//2, y+n//2, n//2)
    ans.append((')')) 

quad_tree(arr, 0, 0, n)
print(''.join(ans))

