N = int(input())
c=list()
for i in range(N):
    dat = list(map(int, input().split()))
    c.append(dat)
c.sort()
for j in c:

    print(*j)
        
    
