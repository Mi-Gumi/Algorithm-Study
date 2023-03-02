N,K = map(int,input().split())

c = []
for _ in range(N):
    c.append(int(input()))
c.sort(reverse= True) # 계산하기 쉬우라고 역순처리


ans = 0 
idx = 0 # 있는 동전을 탐색할 idx
res = K # input으로 들어온 돈
while res != 0:
    if res // c[idx]== 0: # 동전으로 안나눠떨어지면
        idx +=1 # 다음동전으로 넘어가기
    else:
        ans += res//c[idx] # 돈//동전 = 동전의 개수
        res = res%c[idx]   # 남은돈 = 돈을 동전으로 나눈 나머지

print(ans) # 사용한 동전의 개수는 ans와 같다.