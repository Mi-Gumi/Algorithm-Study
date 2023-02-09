import sys
input = sys.stdin.readline

T = int(input())
arr = []
for t in range(T):
    x,y  = map(int, input().split())
    arr.append([x, y]) # x, y좌표를 리스트 형태로 추가

# x좌표, y좌표 순으로, lambda식을 활용해 정렬 진행
arr.sort(key = lambda x: (x[0],x[1]))

for ans in arr:
    print(ans[0], ans[1]) # x, y 출력