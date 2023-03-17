import sys
input = sys.stdin.readline


def ㅣ():
    max_val = 0
    for i in range(N):
        for j in range(M-3):
            sum_val = 0
            for k in range(4):
                sum_val += arr[i][j+k]

            if max_val < sum_val:
                max_val = sum_val

    
    for i in range(N-3):
        for j in range(M):
            sum_val = 0
            for k in range(4):
                sum_val += arr[i+k][j]

            if max_val < sum_val:
                max_val = sum_val      
    return max_val

def ㅁ():
    max_val = 0
    for i in range(N-1):
        for j in range(M-1):
            sum_val = 0
            for k in range(2):
                sum_val += arr[i][j+k]
                sum_val += arr[i+1][j+k]

            if max_val < sum_val:
                max_val = sum_val 

    return max_val

def ㄴ():
    max_val = 0
    for i in range(N-2): #ㄴ 일때
        for j in range(M-1):
            sum_val = 0
            sum_val += arr[i+2][j+1]
            for k in range(3):
                sum_val += arr[i+k][j]

            if max_val < sum_val:
                max_val = sum_val

    for i in range(N-2):  #ㄴ 반대일때 뒤에서 오는걸로
        for j in range(M-1,0,-1):
            sum_val = 0 
            sum_val += arr[i+2][j-1]
            for k in range(3):
                sum_val += arr[i+k][j]
                
            if max_val < sum_val:
                max_val = sum_val
    
    for i in range(N-2): #ㄱ반대일때
        for j in range(M-1):
            sum_val = 0
            sum_val += arr[i][j+1]
            for k in range(3):
                sum_val += arr[i+k][j]

            if max_val < sum_val:
                max_val = sum_val
    
    for i in range(N-2):  #ㄱ 뒤에서 오는걸로
        for j in range(M-1,0,-1):
            sum_val = 0 
            sum_val += arr[i][j-1]
            for k in range(3):
                sum_val += arr[i+k][j]
                
            if max_val < sum_val:
                max_val = sum_val
    
    for i in range(N-1):
        for j in range(M-2):
            sum_val = 0
            sum_val += arr[i+1][j] 
            for k in range(3):
                sum_val += arr[i][j+k]
            
            if max_val < sum_val:
                max_val = sum_val
    
    for i in range(N-1):
        for j in range(M-2):
            sum_val = 0
            sum_val += arr[i+1][j+2] 
            for k in range(3):
                sum_val += arr[i][j+k]
            
            if max_val < sum_val:
                max_val = sum_val
    
    for i in range(N-1,0,-1):
        for j in range(M-2):
            sum_val = 0
            sum_val += arr[i-1][j] 
            for k in range(3):
                sum_val += arr[i][j+k]
            
            if max_val < sum_val:
                max_val = sum_val

    for i in range(N-1,0,-1):
        for j in range(M-2):
            sum_val = 0
            sum_val += arr[i-1][j+2] 
            for k in range(3):
                sum_val += arr[i][j+k]
            
            if max_val < sum_val:
                max_val = sum_val

    return max_val


def ㄹ():
    max_val = 0   #정방향일때
    for i in range(N-2):
        for j in range(M-1):
            sum_val = 0
            for k in range(2):
                sum_val += arr[i+k][j]
                sum_val += arr[i+k+1][j+1]

            if max_val < sum_val:
                max_val = sum_val

    for i in range(N-2): #정 반대방향
        for j in range(M-1,0,-1):
            sum_val = 0
            for k in range(2):
                sum_val += arr[i+k][j]
                sum_val += arr[i+k+1][j-1]

            if max_val < sum_val:
                max_val = sum_val
    
    for i in range(N-1): # ㄷ
        for j in range(M-1,1,-1):
            sum_val = 0
            for k in range(2):
                sum_val += arr[i][j-k]
                sum_val += arr[i+1][j-1-k]

            if max_val < sum_val:
                max_val = sum_val

    for i in range(N-1): # ㄱ
        for j in range(M-2):
            sum_val = 0
            for k in range(2):
                sum_val += arr[i][j+k]
                sum_val += arr[i+1][j+1+k]

            if max_val < sum_val:
                max_val = sum_val
    return max_val

def ㅜ():
    max_val = 0
    for i in range(N-1): #ㅜ
        for j in range(M-2):
            sum_val = 0
            sum_val += arr[i+1][j+1]
            for k in range(3):
               sum_val += arr[i][j+k]
            
            if max_val < sum_val:
                max_val = sum_val

    for i in range(N-1,0,-1): #ㅗ
        for j in range(M-2):
            sum_val = 0
            sum_val += arr[i-1][j+1]
            for k in range(3):
               sum_val += arr[i][j+k]
            
            if max_val < sum_val:
                max_val = sum_val

    for i in range(N-2): #ㅏ 일때
        for j in range(M-1):
            sum_val = 0
            sum_val += arr[i+1][j+1]
            for k in range(3):
                sum_val += arr[i+k][j]

            if max_val < sum_val:
                max_val = sum_val
    
    for i in range(N-2): #ㅓ 일때
        for j in range(M-1,0,-1):
            sum_val = 0
            sum_val += arr[i+1][j-1]
            for k in range(3):
                sum_val += arr[i+k][j]

            if max_val < sum_val:
                max_val = sum_val

    return max_val



N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = [ㅣ(),ㅁ(),ㄹ(),ㄴ(),ㅜ()]
print(max(ans))
