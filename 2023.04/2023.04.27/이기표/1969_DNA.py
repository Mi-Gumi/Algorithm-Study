'''
행으로 탐색하여 Hamming Distance의 합이 가장 작은 DNA 생성
생성한 Hamming Distance의 합은?
'''
def find_H():
    global ans
    target = [[''] for _ in range(M)]
    for j in range(M):
        DNA = [0] * 4 # A C G T
        for i in range(N):
            if arr[i][j] == 'A': DNA[0] += 1
            elif arr[i][j] == 'C': DNA[1] += 1
            elif arr[i][j] == 'G': DNA[2] += 1
            elif arr[i][j] == 'T': DNA[3] += 1
        max_v = DNA[0]
        max_idx = 0
        for k in range(len(DNA)):
            if max_v < DNA[k]:
                max_v = DNA[k]
                max_idx = k
        ans += (N - max_v)
        if max_idx == 0: target[j] = 'A'
        elif max_idx == 1: target[j] = 'C'
        elif max_idx == 2: target[j] = 'G'
        elif max_idx == 3: target[j] = 'T'
    return target

N, M = map(int, input().split())
arr = list(input() for _ in range(N))
ans = 0
rst = find_H()
print(''.join(rst))
print(ans)
