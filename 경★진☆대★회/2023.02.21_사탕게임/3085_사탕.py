N = int(input())
arr = [list(input()) for _ in range(N)]
max_cnt = -1 # 최대길이 및 정답
def count_w(): # 가로를 전체 체크하며 max값 찾기
    global max_cnt
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]: # 다음 글자와 비교
                cnt += 1
            else:
                cnt = 1

            if max_cnt < cnt: # max값 비교
                max_cnt = cnt

def count_h(): # 세로를 전체 체크하며 max값 찾기
    global max_cnt
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if arr[j][i] == arr[j+1][i]: # 다음 글자와 비교
                cnt += 1
            else:
                cnt = 1

            if max_cnt < cnt: # max값 비교
                max_cnt = cnt

for i in range(N): # 가로 글자 바꾸기
    for j in range(N-1):
        if arr[i][j] != arr[i][j+1]: # 다음 글자와 다를 시 위치 변경
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            count_w() # 가로 max 찾기
            count_h() # 세로 max 찾기
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j] # 글자를 다시 원위치

for i in range(N): # 세로 글자 바꾸기
    for j in range(N-1):
        if arr[j][i] != arr[j+1][i]: # 다음 글자와 다를 시 위치 변경
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            count_w() # 가로 max 찾기
            count_h() # 세로 max 찾기
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i] # 글자를 다시 원위치
print(max_cnt)




