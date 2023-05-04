
N = int(input())
E = int(input())

edges = [list(map(int,input().split())) for _ in range(E)]
parents = [i for i in range(N+1)]
edges.sort(key = lambda x:x[2])
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

answer = 0
count = 0
for s, e, w in edges:
    sRoot = find(s)
    eRoot = find(e)

    if sRoot != eRoot:
        if sRoot < eRoot:
            parents[eRoot] = sRoot
        else:
            parents[sRoot] = eRoot
        answer += w

    if count == N-1:
        break
print(answer)