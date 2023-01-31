import sys
T = int(sys.stdin.readline())
li = []
for i in range(T):
    m = int(input())
    li.append(m)
ans = li.copy()    
sorted_m = sorted(li)
list_pop = []
list_push = []
ans_list = []
j = 1
while j:
    if not sorted_m and not list_push:
        break
    if not list_push:
        list_push.append(sorted_m[0])
        sorted_m.pop(0)
        ans_list.append('+')    
    if list_push[-1] != li[0] and not sorted_m:
        ans_list.append(0) 
        break
    elif list_push[-1] == li[0]:
        list_pop.append(list_push[-1])
        list_push.pop(-1)
        li.pop(0)
        ans_list.append('-') 
    elif list_push[-1] != li[0]:
        list_push.append(sorted_m[0])
        sorted_m.pop(0)
        ans_list.append('+')
if 0 in ans_list:
    print('NO')
else :
    for k in range(len(ans_list)):
        print(ans_list[k]) 