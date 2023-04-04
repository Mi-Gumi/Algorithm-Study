N = int(input()) # 기둥의 개수
lh = [list(map(int, input().split())) for _ in range(N)] # L 인덱스 H 높이
lh.sort(lambda x: x[1])
print(lh) # [[5, 3], [2, 4], [11, 4], [4, 6], [13, 6], [15, 8], [8, 10]]
idx = sorted(lh)
print(idx) # [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
mx = lh[-1][1]

hap = 0
for i in range(len(lh)):
    if lh[i][1] < mx:
        hap += (idx[i+1][0] - idx[i][0]) * idx[i][1]
    else:
        abs(lh[-1][0] - lh[-2][0]) * lh[-2][1]


print(hap)
# 가장 작은 면적
