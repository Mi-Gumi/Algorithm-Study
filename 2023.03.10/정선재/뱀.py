N = int(input())
ap = int(input())
ap_list = []
cnt = 0
di = [0,1,0,-1]
dj = [1,0,-1,0]
for i in range(ap):
    a = list(map(int,input().split()))
    ap_list.append(a)
D = int(input())
for j in range(D):
    