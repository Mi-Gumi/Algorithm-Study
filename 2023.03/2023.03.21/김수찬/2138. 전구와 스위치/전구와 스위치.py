N = int(input())

## 시작할 때 켜거나 끌 때에 따라 결과가 달라짐 이 때
## 시작을 할 때 스위치 켜는 것을 구현하기 힘들어서 그냥 cpy 했다.
start = list(map(int, input()))
start_cpy = start[:]
end =  list(map(int, input()))

rlt = 2*N
d= (-1,0,1)

x = 0
is_click = False
# cpy는 첫번째 스위치 켜고 출발
for k in d:
    nx = x + k
    if nx < 0 or nx >= N: continue
    start_cpy[nx] = (start_cpy[nx] + 1) % 2
ans = 0
ans_cpy = 1
x += 1

# 해당 idx의 왼쪽 전구는 앞으로 우리가 선택할 수 없기 때문에,
# 왼쪽 전구의 상태에 따라 켜고 끄는것을 결정

while x < N: # 모든 전구에 대해서
    x_ = x - 1 # 첫번 째 전구를 체크
    if (start[x_] != end[x_]) : # 원본 전구에 대한 if 문
        ans += 1
        for k in d:
            nx = x + k
            if nx < 0 or nx >= N: continue
            start[nx] = (start[nx] + 1) % 2
        pass
    if (start_cpy[x_] != end[x_]) : # 시작할 때 스위치 작업을 한 전구에 대한 if 문
        ans_cpy += 1
        for k in d:
            nx = x + k
            if nx < 0 or nx >= N: continue
            start_cpy[nx] = (start_cpy[nx] + 1) % 2
        pass
    x += 1


# 각각의 조건을 분석 후 min 값을 찾아서 결과를 파악
if start == end:
    rlt = min(ans,rlt)
if start_cpy == end:
    rlt = min(ans_cpy,rlt)
if rlt == 2*N:
    rlt = -1
print(rlt)