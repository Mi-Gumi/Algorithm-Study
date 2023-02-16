import sys
input = sys.stdin.readline

N = int(input())

meeting = [list(map(int,input().split())) for _ in range(N)]
meeting.sort(key= lambda x : x[0])
meeting.sort(key= lambda x : x[1])

ans_list = []

ans_list.append(meeting[0])
i = 1
while i < N :
    if ans_list[-1][1]<=meeting[i][0] :
        ans_list.append(meeting[i])
    i+=1
    
print(len(ans_list))
        