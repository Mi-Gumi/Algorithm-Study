n, length, L = map(int, input().split())

truck = list(map(int, input().split()))
queue = [0] * length  # 다리 큐  , 현재 비어있는 상태
cnt = 0               # 걸린시간
ww = 0                # 다리의 현재 무게
while queue:
    ww -= queue.pop(0) # 다리를 통과한 트럭의 무게 마이너스
    if truck:   # 건널 트럭이 남아 있으면 큐에 추가, 없으면 추가하지 않으므로 마지막은 0이 아님
        if ww + truck[0] <= L:    # 최대하중을 넘지 않으면
            ww += truck[0]        # 무게 추가
            queue.append(truck.pop(0))
        else:
            queue.append(0)  # 0을 추가, 다음 트럭은 기다리고 있음
    cnt += 1                 # 시간 증가
print(cnt)
