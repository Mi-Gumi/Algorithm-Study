import sys

# def calc(N, k, s):
#     global count

    # N 과 K 가 같다면
#     if N == k:
        # s가 나온적이 없다면
#         if not visited[s]:
            # 방문처리
#             visited[s] = 1
            # count + 1
#             count += 1
#         return
    
    # 1, 5, 10, 50 에 대해 각각 다시 calc
#     for i in range(4):
#         calc(N, k + 1, s + num[i])


# N = int(sys.stdin.readline())

# num = [1, 5, 10, 50]
# visited = [0] * 1001
# count = 0

# calc(N, 0, 0)

# print(count)

N = int(sys.stdin.readline())

# 정답 집합 선언
ans = set()

# 1의 갯수
for i in range(N + 1):
    # 전체 갯수에서 1의 갯수를 제외한 5의 갯수
    for j in range(N - i + 1):
        # 전체 갯수에서 1의 갯수와 5의 갯수를 제외한 10의 갯수
        for k in range(N - i - j + 1):
            # 전체 갯수에서 1의 갯수와 5의 갯수, 10의 갯수를 제외한 50의 갯수
            l = N - i - j - k
            # 연산
            num = i + j * 5 + k * 10 + l * 50
            # 집합에 추가
            ans.add(num)

# 집합 길이 출력
print(len(ans))
