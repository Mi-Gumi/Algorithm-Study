N, M = map(int,input().split())
P = list(map(int,input().split()))
# N은 카드 갯수, M은 맞춰야 할 수
# 3<=N<=100, 10<=M<=300,000
c = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            o = P[i]+P[j]+P[k]
            if (c < o) and (M >= o):
                c = o

print(c)



