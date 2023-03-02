from collections import deque
N, W, L = map(int, input().split())
que_truck = deque(map(int, input().split())) # 트럭
que_bridge = deque([0] * W) # 다리
cnt = 0
while que_truck:
    que_bridge.popleft()
    truck = que_truck[0]
    # 다리 위의 트럭과 진입할 트럭합이 하중보다 작고 다리의 남은 길이가 작다면
    if sum(que_bridge) + truck <= L and len(que_bridge) < W:
        que_bridge.append(que_truck.popleft()) # 다리에 트럭 이동
    else:
        que_bridge.append(0) # 트럭 이동 x
    cnt += 1 

print(cnt + W)