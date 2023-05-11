import sys
input = sys.stdin.readline


def subset(n, idx):
    # 6개의 번호를 모두 골랐다면 출력
    if n == 6:
        print(*ans)
        return
    
    for i in range(idx + 1, k - 5 + n):
        ans.append(arr[i])
        subset(n + 1, i)
        ans.pop()


arr = list(map(int, input().split()))
while arr[0]:
    k = arr.pop(0)
    ans = []
    subset(0, -1)
    print()
    arr = list(map(int, input().split()))