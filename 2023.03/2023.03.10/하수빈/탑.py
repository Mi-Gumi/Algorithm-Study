import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
stack = []
ans = []
i = 0

# 마지막 탑 까지 반복
while i < N:
    # 스택에 요소가 있다면
    if stack:
        # 스택의 마지막 탑 길이가 현재 탑 길이 보다 길다면
        if stack[-1][1] > top[i]:
            # 현재 탑 신호는 스택의 마지막 탑에서 가로막힘으로 ans에 스택의 마지막 탑 인덱스 + 1 추가
            ans.append(stack[-1][0] + 1)
            # 스택에 현재 탑의 인덱스와 현재 탑의 높이 추가
            stack.append([i, top[i]])
            # 인덱스 + 1
            i += 1
        # 스택의 마지막 탑 길이가 현재 탑 길이 보다 작다면
        else:
            # 스택의 마지막 탑으로 신호가 올 일이 없으므로 pop
            stack.pop()
    # 스택에 요소가 없다면
    else:
        # 현재 탑의 인덱스와 현재 탑의 높이 추가
        stack.append([i, top[i]])
        # 앞에 현재 탑보다 큰 탑이 없으므로 ans에 0 추가
        ans.append(0)
        # 인덱스 + 1
        i += 1

print(*ans)