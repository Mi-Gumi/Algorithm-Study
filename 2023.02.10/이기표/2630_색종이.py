import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

white_blue_check = [0, 0]
def divide(arr, x, y, n): # arr도 쪼개서 저장
    white_cnt = blue_cnt = 0

    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] == 0:
                white_cnt += 1
            else:
                blue_cnt += 1    
    
    if white_cnt == n ** 2:
        white_blue_check[0] += 1
        return

    if blue_cnt == n ** 2:
        white_blue_check[1] += 1
        return
                
    divide(arr, x, y, n//2)
    divide(arr, x, y+n//2, n//2)
    divide(arr, x+n//2, y, n//2)
    divide(arr, x+n//2, y+n//2, n//2)
    
divide(arr, 0, 0, n)
print(white_blue_check[0],white_blue_check[1], sep='\n')