from itertools import permutations

k = int(input())

boo = input().split()

numbers = [0,1,2,3,4,5,6,7,8,9]

pm = list(permutations(numbers,k+1))
len_pm = len(pm)
for j in range(len_pm) :
    p = pm[j]
    for i in range(k):
        if boo[i] == '<' :
            if p[i] < p[i+1] :
                continue
            else :
                break
        else :
            if p[i] > p[i+1] :
                continue
            else :
                break
    else :
        _min = p
        break
for j in range(len_pm-1,-1,-1) :
    p = pm[j]
    for i in range(k):
        if boo[i] == '<' :
            if p[i] < p[i+1] :
                continue
            else :
                break
        else :
            if p[i] > p[i+1] :
                continue
            else :
                break
    else :
        _max = p
        break

print(*_max, sep='')
print(*_min,sep='')