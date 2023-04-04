N = int(input())
tower = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append((i, tower[i]))

print(*answer)

# 신호가 오른쪽에서 보내지지만, 받는 쪽 기준으로 생각
# 좌측 부터 유의미한 탑의 높이만 stack에 남김
