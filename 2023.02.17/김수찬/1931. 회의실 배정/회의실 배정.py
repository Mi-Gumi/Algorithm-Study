N = int(input())

r = []
for _ in range(N):
    r.append(list(map(int,input().split())))

r.sort(key = lambda x: (x[1], x[0])) # 회의실의 시작과 끝을 맞춰줘야함
## 파이썬 짱짱맨.. 이게 단 한줄이네 ㅋㅋ

# end가 가장 작은 순서, 이후 그리고 start가 가장 작은 순서로 배열을 만들면
# end와 next_start 의 차이가 가장 작은 지점 대로 나아가는 것이 
# 가장 회의실을 많이 배정할 수 있음 

cnt = 1
end_time = r[0][1] # end가 가장 작은게 우선순위로 정렬시켰기 때문에,
# 이것으로 시작하는게 가장 빠를것이라 예상
for i in range(1, N):
    if r[i][0] >= end_time: # 다음 회의의 시작이 end time과 같거나 커야 다음회의가 진행
        cnt += 1 # 다음 회의 카운팅
        end_time = r[i][1]
print(cnt) # 카운팅한 결과 출력