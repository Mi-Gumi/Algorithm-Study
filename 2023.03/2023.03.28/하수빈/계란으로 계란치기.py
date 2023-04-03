import sys
input = sys.stdin.readline

def crash(idx):
    global ans
    # 끝까지 오면
    if idx == N:
        tmp = 0
        # 깨진 달걀 갯수 파악
        for e in egg:
            if e[0] <= 0:
                tmp += 1
        if ans < tmp:
            ans = tmp
        return
    
    # 현재 달걀이 깨졌다면
    if egg[idx][0] <= 0:
        # 다음 달걀으로 이동
        crash(idx + 1)
    else:
        flag = 1
        for i in range(N):
            # 달걀을 깰 수 있다면
            if i != idx and egg[i][0] > 0:
                egg[idx][0] -= egg[i][1]
                egg[i][0] -= egg[idx][1]
                crash(idx + 1)
                # 달걀을 깼다는 표시
                flag = 0
                egg[idx][0] += egg[i][1]
                egg[i][0] += egg[idx][1]
        # 달걀을 못깼다면 다음달걀으로 이동
        if flag:
            crash(idx + 1)
                

N = int(input())
egg = [list(map(int, input().split())) for _ in range(N)]
ans = 0
crash(0)
print(ans)