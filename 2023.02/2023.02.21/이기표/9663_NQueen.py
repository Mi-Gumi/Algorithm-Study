'''
인덱스로 접근하여 열, 대각, 역대각 팀색
'''
def nqueen(n):
    global cnt
    if n == N: # 해당 깊이까지 도달하면 경우의 수 증가
        cnt += 1
        return

    for i in range(N):
        if not visited_1[i] and not visited_2[n+i] and not visited_3[n-i]: # 방문처리가 안되어있는 경우
            visited_1[i] = visited_2[n+i] = visited_3[n-i] = True # 방문처리
            nqueen(n+1)
            visited_1[i] = visited_2[n+i] = visited_3[n-i] = False # 원위치

N = int(input())
visited_1 = [False] * N # 열 탐색
visited_2 = [False] * (2*N-1) # 대각 탐색 -> 대각 규칙 각 좌표의 합이 같다.
visited_3 = [False] * (2*N-1) # 역대각 탐색 -> 역대각 규치 각 좌표의 차가 같다.
cnt = 0 # 경우의 수

nqueen(0) # 0 깊이부터 탐색
print(cnt)