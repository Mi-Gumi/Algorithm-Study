import sys
input = sys.stdin.readline

N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

# 로프 내림차순 정렬
rope.sort(reverse=True)
# 중량 최댓값 선언
max_w = 0

# 로프를 내림차순으로 정렬하면 로프의 갯수 * 로프의 최대 중량이 그 로프의 중량 최댓값이 된다.
for i in range(len(rope)):
    max_w = max(max_w, rope[i] * (i + 1))

print(max_w)