a = list(map(str,input()))
b = list(map(str,input()))


i = 0
flag = 1
while flag:
    if a[i] == b[0]:
        cnt = 0
        for j in range(len(b)):
            
            if a[i+j] == b[j]:
                cnt += 1
                           
        if cnt == len(b):
            for k in range(len(b)):
                a.pop(i)              
            i = 0
        else:
            i += 1                 
    
    else:
        i += 1
    if i >= (len(a)):
        flag = 0
        break
if len(a) != 0:
    print(*a, sep ='')
else:
    print('FRULA')