import math

N = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))

min = +1e9
max = -1e9

def devide(a,b):
  rlt = math.floor(a//b) if a*b >= 0 else - math.floor(abs(a)//abs(b))
  return rlt


def dfs(depth, compare):  
    global oper, min, max # 전역변수 등록해야 업데이트 됨
    if(sum(oper) == 0):
        if(compare > max): max = compare
        if(compare<min): min = compare
        return
    
    if(oper[0]>0):
        oper[0] -= 1
        dfs(depth+1, compare + numbers[depth])
        oper[0] += 1
        
    if(oper[1]>0):
        oper[1] -= 1
        dfs(depth+1, compare - numbers[depth])
        oper[1] += 1
        
    if(oper[2]>0):
        oper[2] -= 1
        dfs(depth+1, compare * numbers[depth])
        oper[2] += 1
        
    if(oper[3]>0):
        oper[3] -= 1
        dfs(depth+1, devide(compare,numbers[depth]))
        oper[3] += 1    

dfs(1,numbers[0])
print(max)
print(min)
