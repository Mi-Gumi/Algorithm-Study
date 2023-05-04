'''
사다리는 최대 3개까지 조작가능 -> 3보다 크면 -1 출력
완전 탐색
'''
import pprint

def itoi(): #i번째에서 i번째를 확인
    for i in range(N):
        pos = i
        for j in range(H):
            if arr[j][pos]:
                pos += 1 # 오른쪽으로 이동
            elif pos > 0 and arr[j][pos-1]:
                pos -= 1 # 왼쪽으로 아동
        # 첫번째와 값이 동일하지 않은 경우
        if pos != i:
            return 0
    # 첫번쨰와 값이 동일
    return 1

def dfs(x, y, line):
    global cnt
    if itoi(): # 최소 이동횟수 최신화
        cnt = min(cnt, line)
        return
    elif line == 3 or cnt <= line: # 3회 또는 최소 이동횟수보다 크면 종료
        return

    # 완전 탐색 진행
    for i in range(x, H):
        pos = y if i == x else 0
        for j in range(pos, N-1):
            # 왼쪽과 오른쪽이 둘 다 비었을 때 진행
            if arr[i][j] == 0 and arr[i][j+1] == 0 and arr[i][j-1] == 0:
                arr[i][j] = 1 # 사다리 놓기
                dfs(i, j+2, line+1)
                arr[i][j] = 0 # 사다리 해제


N, M, H = map(int, input().split())
arr = [[0]*N for _ in range(H)] # 2차원 배열 생성
for _ in range(M):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

cnt = 4
dfs(0, 0, 0)
if cnt < 4:
    print(cnt)
else:
    print(-1)


