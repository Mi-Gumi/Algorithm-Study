'''
스택을 통해 인덱스의 값을 비교해가며 넓이 구하기
'''
while 1:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break

    N = lst[0]
    lst = lst[1:]
    stack = []
    max_v = 0
    for i in range(N):
        idx = i # 인덱스
        while stack and stack[-1][1] > lst[i]: # 큰 값을 만날때까지 꺼내기
            idx, height = stack.pop()
            rst = (i - idx) * height # (현재 인덱스 - 스택에서 꺼낸 인덱스) = 가로 길이 / 가로 * 세로
            max_v = max(max_v, rst) # 최고 넓이 갱신
        stack.append((idx, lst[i])) # 스택에 추가

    while stack: # 마지막에 남은 값을
        idx, height = stack.pop()
        rst = (N - idx) * height
        max_v = max(max_v, rst)
    print(max_v)


