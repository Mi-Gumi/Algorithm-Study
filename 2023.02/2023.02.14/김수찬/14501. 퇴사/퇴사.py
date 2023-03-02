N = int(input())
sang = [[0,0]]
for i in range(N):
    sang += [list(map(int,input().split()))]

rlt = set()
def dfs(now, benefit):
    if sang[now][0] + now > N : 
        if sang[now][0] + now != N+1:
            benefit -= sang[now][1]
        rlt.add(benefit)
        return
    
    for i in range(now+1, len(sang)):
        need, pay = sang[i][0], sang[i][1] # 근무일, 돈
        a = sang[now][0] # 현재 근무 일자
        b = i - now # 근무 진행 정도
        
        # 현재 근무 일자보다, 근무 진행 정도가 클경우, continue
        if sang[now][0] > i - now : continue
        ## 퇴사 전날에 상담이 올 경우
        ## 받은 상담날짜 + 현재 >= 퇴사일
        c = sang[i][0]
        d = i
        
        #위 조건 모두 만족하면 입금받음
        benefit += pay
        dfs(i, benefit)
        benefit -= pay


dfs(0,0)
print(max(rlt))