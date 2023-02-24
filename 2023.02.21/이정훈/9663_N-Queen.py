def backtracking(n, k, last):
    # n : 체스판의 길이, k : 재귀 깊이 , last : 현재 놓은 자리의 index
    global cnt
    # 후보 리스트          0:후보 , 1:불가능
    candidate = [0] * N

    # 지금까지 놓은 퀸의 수만큼  처음에는 k= 0이기때문에 pass 함
    for i in range(k):
        #  퀸은 가로세로, 대각선으로 움직일 수 있기 때문에 한줄에 하나만 놓을 수 있음
        #  퀸을 놓으면 왼쪽 아래 대각선, 수직, 오른쪽아래 대각선에는 다른 퀸을 놓을 수 없음
        #  대각선은 칸이 멀어질 수로 대각선의 위치도 뻗어나감 (현재깊이 - 퀸의깊이) 만큼

        # 수직
        candidate[last[i]] = 1
        # 왼쪽 대각선
        if 0 <= last[i] - (k - i):            # 인덱스 체크
            candidate[last[i] - (k - i)] = 1
        # 오른쪽 대각선
        if N > last[i] + (k - i):
            candidate[last[i] + (k - i)] = 1

    if sum(candidate) == N:   # 백트래킹하는 부분 ( 모두 1이면 후보가 없음 )
        return

    for i in range(N):
        if candidate[i] == 0:
            # 후보이면서 깊이가 n-1이면 마지막 퀸이기 때문에 카운트하고 continue
            if k + 1 == n:
                cnt += 1
                continue
            last.append(i)  # 놓아보고
            backtracking(n, k + 1, last)
            last.pop()      # 아님말고


N = int(input())
cnt = 0
stack = []

backtracking(N, 0, stack)

print(cnt)
