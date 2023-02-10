N = int(input())

# 분할탐색 진행
def daq(target, length ,cnt):
    if target <= 3:
        return 'm' if target == 1 else 'o'

    count = cnt + 3   # 중간에 있는 mooo 의 크기
    pre = length      # S(n)번째 moo배열의 S(n-1)번째 moo 
    mid = pre + count # 중간에 있는 mooo 끝
    next_length = length*2 + count # S(n)번째 moo배열의 마지막
    
    pre_length = (length - (count-1))//2 # S(n-1)번째 moo의 S(n-2)번째 moo 
    pre_mid = pre_length + (count-1)     # S(n-1)번째 moo의 중간
    pre_end = pre_length*2 + (count-1)   # S(n-1)번째 moo의 마지막 -> pre와 동일해야한다.
    
    if target > next_length: # 목표하는 값이 next_length보다 클 경우
        return daq(target, next_length, cnt+1) # 확장을 진행

    elif target <= pre: # 목표하는 값이 S(n-1) 값 보다 작을 경우 -> S(n-1)로 이동
        target = target - pre if target - pre > 0 else target  # 뒤에 있는 친구가 올 경우, target 의 위치는 그냥 target 
        return daq(target, pre_length, cnt-1)
    elif target <= mid: # 목표하는 값이 중간의 mooo 에 존재할 경우
        return 'm' if target == pre + 1 else 'o' # 중간 mooo 의 첫번째는 pre +1
    elif target <= next_length: # 목표하는 값이 중간보다는 큰데, 최대값 보다 값 보다 작을 경우
        return daq(target-mid, pre_length, cnt-1) # S(n-1)로 이동
    

# 목표지점, 초기값, (depth => mid 에 있는 mooo 분석용)
ans = daq(N, 3, 1)
print(ans)