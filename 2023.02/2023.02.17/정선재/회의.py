import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x : x[0])
arr.sort(key = lambda x : x[1])
count = 0
_list = arr[0]
for i in range(1,len(arr)):
    if _list[1] <= arr[i][0]:
        _list = arr[i]
        count += 1
    


print(count+1)
