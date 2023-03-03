N = int(input())

r = [] # 문자열을 넣는 리스트
temp = 0 # 리스트 길이 최댓값 찾기
for _ in range(N):
    txt = list(input())
    if len(txt) > temp:
      temp = len(txt)
    r.append(txt)
###################################

# 2차원 배열 형태로 변환하기 위해 작업
for i in range(N):
  r[i] = ['0']*(temp - len(r[i])) + r[i]
  
num_dic = dict() # 문자열을 숫자 형태로 바꾸기 위한 dict
for j in range(temp): # 열 방향 탐색
  for i in range(N):  # 행 방향 탐색
    if r[i][j] == '0': continue # 임의로 만든 0 이 있을 경우 넘어감
    if not num_dic.get(r[i][j]): # diction 형태로 저장
      num_dic.setdefault(r[i][j], 0) # 처음에는 cnt를 했지만, 반례가 있음..

    
    num_dic[r[i][j]] += 10**((temp-1)-j) ## 그래서 가중치 뒀음


# print(num_dic)
x = list(num_dic.items())
x.sort(key = lambda x: (-x[1]))
# print(x)
ans = 0
for i in range(len(x)):
  ans += (9-i)*x[i][1]
print(ans)