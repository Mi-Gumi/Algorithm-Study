def dfs(k, tmpset) :
    global min_blank
    if k == CCTV_COUNT :
        # print(tmpset)
        blank = total_blank - len(tmpset)
        if min_blank > blank :
            min_blank = blank
        return
    for cover in cctv_cover[k] :
        dfs(k+1, tmpset|cover )  # 감시 구역을 합집합 연산하여 dfs 호출

n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

# 방향 별 di, dj
d = ((0,1),(1,0),(0,-1),(-1,0))

# cctv의 회전 경우의 수별 감시방향
CCTV = {
    1:((0,),(1,),(2,),(3,)),   # 한방향 4가지
    2:((0,2),(1,3)),
    3:((0,1),(1,2),(2,3),(3,0)),
    4:((0,1,2),(0,1,3),(0,2,3),(1,2,3),),
    5:((0,1,2,3),),  # 네방향 1가지
}

cctvs = []
total_blank = 0
for i in range(n) :
    for j in range(m) :
        # 0의 개수 count
        if arr[i][j] == 0 :
            total_blank += 1
        # cctv 위치 및 종류 저장
        elif 1<= arr[i][j] <= 5 :
            cctvs.append((i,j,arr[i][j]))
# cctv의 개수
CCTV_COUNT = len(cctvs)
min_blank = total_blank

cctv_cover = [[set()] for _ in range(CCTV_COUNT)]
# cctv개수만큼
for i in range(CCTV_COUNT) :
    si, sj, num = cctvs[i]
    # 회전 경우의 수 만큼

    for watch in CCTV[num] :
        cover = set()

        for direction in watch :  # 감시할 수 있는 방향
            di, dj = d[direction]
            # 일직선으로

            for k in range(n+m) :

                ni , nj = si + k*di, sj + k*dj

                if 0<=ni<n and 0<=nj<m :
                    if arr[ni][nj] == 6 :
                        break
                    elif arr[ni][nj] == 0 :
                        cover.add((ni,nj)) # 감시구역에 추가
                else :
                    break
        # 회전방향의 감시구역 집합이 비어있지 않다면 추가
        if cover :
            cctv_cover[i].append(cover)

# print(cctv_cover)
dfs(0, set())
print(min_blank)

