def backtracking(n, k, last):
    global cnt

    candidate = [0] * N
    for i in range(k):
        candidate[last[i]] = 1
        if 0 <= last[i] - (k - i):
            candidate[last[i] - (k - i)] = 1
        if N > last[i] + (k - i):
            candidate[last[i] + (k - i)] = 1
    if sum(candidate) == N:
        return

    for i in range(N):
        if candidate[i] == 0:
            if k + 1 == n:
                cnt += 1
                continue
            last.append(i)
            backtracking(n, k + 1, last)
            last.pop()


N = int(input())
cnt = 0
stack = []

backtracking(N, 0, stack)

print(cnt)
