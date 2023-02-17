import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    k = int(input())
    arr.append(k)

arr.sort(reverse=True)
max_ans = 0

for i in range(len(arr)): # 1개 사용 제일 높은 값 / N개 사용 제일 낮은값 * N
    tmp = arr[i] * (i+1)

    if max_ans < tmp:
        max_ans = tmp

print(max_ans)