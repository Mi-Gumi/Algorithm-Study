import sys

text = sys.stdin.readline().rstrip()
bmb = sys.stdin.readline().rstrip()
b = len(bmb)
ans = list()

for i in range(len(text)):
  ans.append(text[i]) ## ans에 문자 하나를 넣음
  
  # ans[-b:]는 error 가 안남을 이용함 
  if ''.join(ans[-b:]) == bmb: # 뒤의 문자가 bom이랑 동일하면 
    for _ in range(b): # 지워버린다.
        ans.pop()

if ans: # 연산이 끝났을 때 ans 가 비워져있지 않으면
  print(''.join(ans))
else: # 비워져있으면
  print('FRULA')
  