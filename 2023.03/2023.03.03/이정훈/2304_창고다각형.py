N = int(input())

support = [list(map(int, input().split())) for _ in range(N)]
_max = 0   # 최대값
_max_idx = 0  # 최대값의 index
_max_range = 0  # 지붕의 길이


for L, H in support:
    # 최대길이 저장
    if L > _max_range:
        _max_range = L
    # 최대값과 인덱스 저장
    if _max < H:
        _max = H
        _max_idx = L

# 길이에 맞게 리스트 생성
arr = [0] * (_max_range + 1)

# 값 매핑
for L, H in support:
    arr[L] = H

_sum = 0    # 넓이

_max_tmp = arr[0]
# 좌측부터 최대값전까지
for i in range(_max_idx):
    if arr[i] > _max_tmp:
        _max_tmp = arr[i]
    _sum += _max_tmp

_max_tmp = arr[-1]
# 우측부터 최대값까지
for i in range(_max_range, _max_idx - 1, -1):
    if arr[i] > _max_tmp:
        _max_tmp = arr[i]
    _sum += _max_tmp

print(_sum)
