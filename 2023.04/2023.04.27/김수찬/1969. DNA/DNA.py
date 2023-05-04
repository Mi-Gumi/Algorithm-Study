def check(i,j):
    if dnas[i][j] == 'A' : return 0
    if dnas[i][j] == 'C' : return 1
    if dnas[i][j] == 'G' : return 2
    if dnas[i][j] == 'T' : return 3

def rev(x):
    if x == 0 : return 'A'
    if x == 1 : return 'C'
    if x == 2 : return 'G'
    if x == 3 : return 'T'

N, M = map(int,input().split())
dnas = [list(input()) for _ in range(N)]

ans = []
for j in range(M):
    acgt = [0, 0, 0, 0]
    for i in range(N):
        target = check(i,j)
        acgt[target] += 1
    x = acgt.index(max(acgt))
    ans.append(rev(x))
    
print(''.join(ans))
cnt = 0
for i in range(N):
    for j in range(M):
        if ans[j] != dnas[i][j]:
            cnt += 1
            
print(cnt)