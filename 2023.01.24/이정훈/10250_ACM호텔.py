T = int(input())
H = []
W = []
N = []
for i in range(T) :
    a,b,c = map(int,input().split())
    H.append(a)
    W.append(b)
    N.append(c)
for i in range(T) :
    if N[i]%H[i] == 0 :
        floor = H[i]
        ho = N[i]//H[i]
    else :
        floor = N[i]%H[i]
        ho = N[i]//H[i]+1
    room = floor*100+ho
    print(room)