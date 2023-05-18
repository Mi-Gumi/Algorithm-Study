n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

d = ((0,-1),(1,0),(0,1),(-1,0))
dd = ((0,1),(-1,0),(0,-1),(1,0))

spread = ((-2, 0, 2),(-1, -1, 10),(-1, 0, 7),(-1, 1, 1),(0, -2, 5),(1, -1, 10),(1, 0, 7),(1, 1, 1),(2, 0, 2))

dir_grid = [[5]*n for _ in range(n)]

center = n//2
i, j = 0, 0
look = 0
while not ((i , j) == (center, center)) :
    dir_grid[i][j] = look
    di, dj = dd[look]
    ni, nj = i+di, j+dj
    if 0 > ni or ni >= n or nj < 0 or nj >= n  or dir_grid[ni][nj] != 5:
        dir_grid[i][j] = look
        look = (look-1) % 4
        di, dj = dd[look]
        i, j = i+di, j+dj
        continue
    i, j = ni, nj
dir_grid[center][center] = 0



ti, tj = center, center
look = 0
out_sand = 0
while not (ti == 0 and tj == 0) :
    look = dir_grid[ti][tj]
    di, dj = d[look]
    ni, nj = ti + di, tj + dj
    if 0 > ni or ni >= n or nj < 0 or nj >= n :
        look = (look+1) % 4
        di, dj = d[look]
        ni, nj = ti + di, tj + dj
    sand = grid[ni][nj]
    for spread_di, spread_dj, percent in spread :
        if look == 3 : 
            spread_di, spread_dj = spread_dj, spread_di
        elif look == 1 :
            spread_di, spread_dj = spread_dj, spread_di
            spread_di *= -1
        elif look == 2 :
            spread_dj *= -1
        spread_sand = sand * percent // 100
        grid[ni][nj] -= spread_sand 
        spread_ni , spread_nj = ni + spread_di, nj + spread_dj

        if 0 > spread_ni or spread_ni >= n or spread_nj < 0 or spread_nj >= n :
            out_sand += spread_sand
        else :
            grid[spread_ni][spread_nj] += spread_sand
    alpha_i, alpha_j = ni + di, nj + dj 
    if 0 > alpha_i or alpha_i >= n or alpha_j < 0 or alpha_j >= n :
        out_sand += grid[ni][nj]
    else :
        grid[alpha_i][alpha_j] += grid[ni][nj]
    grid[ni][nj] = 0
    ti , tj = ni, nj
    # print(ti, tj)
    # print(out_sand)

    # print(*grid, sep='\n')
print(out_sand)