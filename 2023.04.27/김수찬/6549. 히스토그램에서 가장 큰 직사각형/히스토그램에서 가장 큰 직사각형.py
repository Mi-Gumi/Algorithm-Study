while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break
    
    N = lst[0]
        
    stack = []
    max_rlt = 0
    
    for i in range(1, N+1):
        height = lst[i]
        if stack and stack[-1][1] > height:
            while stack:  # 스택에서 빼내며 최대 직사각형 넓이를 계산
                stack_i, stack_height = stack.pop()
                width_start = 1
                if stack:
                    width_start = stack[-1][0]+1
                result = (i - width_start) * stack_height
                max_rlt = max(result, max_rlt) # 최대값 갱신
                # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산
                if not stack or stack[-1][1] <= height:
                    break
        # 스택이 비어 있거나 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 크거나 같으면
        if not stack or stack[-1][1] <= height:
            stack.append((i, height))  # 스택에 현재 막대기를 추가
            
    # 반복이 종료되고, 스택에 남은 막대기가 있다면 계산
    while stack:
        stack_i, stack_height = stack.pop()
        width_start = 1
        if stack:
            width_start = stack[-1][0]+1
        result = (lst[0]+1 - width_start) * stack_height
        max_rlt = max(result, max_rlt) # 최대값 갱신  
        
    print(max_rlt)
