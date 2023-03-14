from collections import deque

N,W,L = map(int,input().split())

start = deque(map(int,input().split()))
bridge = deque([0 for _ in range(W)])

## 브릿지에 존재하는 트럭과 남은 트럭을 이용하여 문젤를 플 것임

cnt = 0
while start or bridge: 
    bridge.popleft()
    if len(start):
        ## For 문을 쓴 거는 이전에 있던 것의 잔재...
        ## 최소로 줄일 수 있도록 트럭을 재배치하는 실수를 했었다..
        for i in range(len(start)): 
            temp = start[i] 
        ## 만약 sum(bridge) + temp >L 이라면 트럭을 올릴 수 없음
        ## bridge에 아무것도 올라가지 않기에 0 을 올림
            if int(sum(bridge) + temp)> L:
                bridge.append(0)
                break
        ## 트럭을 올릴 수 있다면
        ## bridge에 트럭을 올림 
            else:
                start.remove(temp)
                bridge.append(temp)
                break
    cnt+=1 # 각 케이스 마다  cnt를 진행
print(cnt)