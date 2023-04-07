N = int(input())
matrix = list()
for _ in range(N):
    matrix.append(list(map(int,input().split())))

start = 0
end = 5

ans = 0
def sol(s,matrix):
    global ans
    if s == end:
        for i in range(N):
            for j in range(N):
                if matrix[i][j] > ans:
                    ans = matrix[i][j]
        return 
    for i in range(4):
        cpy_matrix = [arr[:] for arr in matrix]## deep copy 보다 6배 빠름
        if i == 0:
            sol(s+1, left(cpy_matrix))
        elif i == 1:
            sol(s+1, right(cpy_matrix))
        elif i == 2:
            sol(s+1, up(cpy_matrix))
        else : # i == 3
            sol(s+1, down(cpy_matrix))


def left(mat):
    for i in range(N):
        target = 0
        for j in range(N):
            if mat[i][j] != 0:
                temp = mat[i][j] # 이동할 정보 저장
                mat[i][j] = 0    # 이동해야하니까 0 으로 바꾸기

                if mat[i][target] == temp: # 타겟이랑 숫자가 같으면
                    mat[i][target] = temp * 2 # a+a 이므로 2a
                    target += 1 # 타겟 지점을 이동시킴
                elif mat[i][target] == 0: # 움직일 위치가 비었으면
                    mat[i][target] = temp # 타겟 위치를 이동시킴
                else : # mat[i][target] != 0 위치에 item이 있으면
                    target += 1
                    mat[i][target] = temp
    return mat


def right(mat):
    for i in range(N-1,-1,-1):
        target = N-1
        for j in range(N-1, -1, -1):
            if mat[i][j] != 0:
                temp = mat[i][j] # 이동할 정보 저장
                mat[i][j] = 0    # 이동해야하니까 0 으로 바꾸기

                if mat[i][target] == temp: # 타겟이랑 숫자가 같으면
                    mat[i][target] = temp * 2 # a+a 이므로 2a
                    target -= 1 # 타겟 지점을 이동시킴
                elif mat[i][target] == 0: # 움직일 위치가 비었으면
                    mat[i][target] = temp # 타겟 위치를 이동시킴
                else : # mat[i][target] != 0 위치에 item이 있으면
                    target -= 1
                    mat[i][target] = temp
    return mat


def up(mat):
    for j in range(N-1,-1,-1):
        target = N-1
        for i in range(N-1, -1, -1):
            if mat[i][j] != 0:
                temp = mat[i][j] # 이동할 정보 저장
                mat[i][j] = 0    # 이동해야하니까 0 으로 바꾸기

                if mat[target][j] == temp: # 타겟이랑 숫자가 같으면
                    mat[target][j] = temp * 2 # a+a 이므로 2a
                    target -= 1 # 타겟 지점을 이동시킴
                elif mat[target][j] == 0: # 움직일 위치가 비었으면
                    mat[target][j] = temp # 타겟 위치를 이동시킴
                else : # mat[i][target] != 0 위치에 item이 있으면
                    target -= 1
                    mat[target][j] = temp
    return mat


def down(mat):
    for j in range(N):
        target = 0
        for i in range(N):
            if mat[i][j] != 0:
                temp = mat[i][j] # 이동할 정보 저장
                mat[i][j] = 0    # 이동해야하니까 0 으로 바꾸기

                if mat[target][j] == temp: # 타겟이랑 숫자가 같으면
                    mat[target][j] = temp * 2 # a+a 이므로 2a
                    target += 1 # 타겟 지점을 이동시킴
                elif mat[target][j] == 0: # 움직일 위치가 비었으면
                    mat[target][j] = temp # 타겟 위치를 이동시킴
                else : # mat[i][target] != 0 위치에 item이 있으면
                    target += 1
                    mat[target][j] = temp
    return mat


sol(start,matrix)
print(ans)