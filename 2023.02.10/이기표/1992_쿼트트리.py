import sys
# input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
ans = []
def quad_tree(arr, x, y, n):
    zero_cnt = one_cnt = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j]:
                one_cnt += 1
            else:
                zero_cnt += 1
    if one_cnt == n**2:
        ans.append('1')
        return

    if zero_cnt == n**2:
        ans.append('0')
        return   
   
    ans.append(('('))
    quad_tree(arr, x, y, n//2)
    quad_tree(arr, x, y+n//2, n//2)
    quad_tree(arr, x+n//2, y, n//2)
    quad_tree(arr, x+n//2, y+n//2, n//2)
    ans.append((')')) 

quad_tree(arr, 0, 0, n)
print(''.join(ans))

