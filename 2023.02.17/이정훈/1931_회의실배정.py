import sys
input = sys.stdin.readline

N = int(input())

meeting = [list(map(int,input().split())) for _ in range(N)]
# 시작시간 기준으로 오름차순 정렬, 종료시간 기준으로 오름차순 정렬
meeting.sort(key= lambda x : x[0])
meeting.sort(key= lambda x : x[1])

ans_list = []
# 종료시간이 가장빠른 회의 바로 추가
ans_list.append(meeting[0])
i = 1
while i < N :
    # 마지막으로 넣은 회의 종료시간 이상이면 , 아니면 i 만 증가로 pass
    if ans_list[-1][1]<=meeting[i][0] :
        ans_list.append(meeting[i])
    i+=1
    
print(len(ans_list))
        