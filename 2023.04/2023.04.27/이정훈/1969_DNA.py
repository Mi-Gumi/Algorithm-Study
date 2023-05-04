n, m = map(int,input().split())

dna = [list(input()) for _ in range(n)]

count = {
    'A' :0,
    'C' :0,
    'G' :0,
    'T' :0,
}

s = ''
for i in range(m) :
    for r in ('A','C','G','T') :
        count[r] = 0
    for j in range(n) :
        count[dna[j][i]] += 1
    s += max(count.keys(),key=lambda x : count[x])

ans = 0
for i in range(n) :
    for j in range(m):
        if dna[i][j] != s[j] :
            ans += 1


print(s)
print(ans)
