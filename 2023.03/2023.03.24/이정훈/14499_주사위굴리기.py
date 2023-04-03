N, M, x, y, K = map(int,input().split())
direc_dict = {
    1 : (0,1), 2 : (0,-1), 3 : (-1,0), 4: (1,0),
}

Map = []
for i in range(N) :
    Map.append(list(map(int,input().split())))
news = list(map(int,input().split()))

d1, d2, d3, d4, d5, d6 = 0,0,0,0,0,0
#   2
# 4 1 3
#   5
#   6
for d in news :
    dx, dy = direc_dict[d]
    nx, ny = x+ dx , y + dy
    
    if 0<= nx < N and 0 <= ny < M :
        if d == 1 :
            d3, d1, d4, d6 = d6, d3, d1, d4
        elif d == 2 :
            d3, d1, d4, d6 = d1, d4, d6, d3
        elif d == 3 :
            d2, d1, d5, d6 = d6, d2, d1, d5
        else :
            d2, d1, d5, d6 = d1, d5, d6, d2
        if Map[nx][ny] == 0 :
            Map[nx][ny] = d1
        else :
            d1 = Map[nx][ny]
            Map[nx][ny] = 0
        x, y = nx, ny
        print(d6)