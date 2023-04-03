
N, C = map(int, input().split()) # N개 집 C개 공유기
home = [int(input()) for _ in range(N)] # 집 좌표

# print(home) # [1, 2, 8, 4, 9]

home.sort()

# print(home) # [1, 2, 3, 4, 8, 9] 예제 1 -> 답: 3 (1~4)
              #  +        +  +
              #  +        +     +

# 가운데를 중심으로 공유기 C개 배분
# 2개는 무조건 처음과 끝에 배분

start = 0
end = N-1

for i in range(N):
    mid = (start + end) // 2

    if home[mid] < N // 2:
        start += 1

# 따흑흑
