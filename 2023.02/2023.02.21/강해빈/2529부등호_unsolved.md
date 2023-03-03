```python
from itertools import permutations
k = int(input())
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = list(permutations(num, k+1)) # [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 1, 6), ...
sign = list(map(str, input().split())) # ['<', '>']

aa = [] # 튜플 형태 리스트로 바꾸기 [[0, 1, 2], [0, 1, 3], ...
for i in n:
    a = list(i)
    aa.append(a)

re = []
def back(): # 백트래킹은 뭘까...
    if len(re) == k+1:
        print(re)
        return

    for j in aa:
        # print(j)
        for q in range(k):
            if sign[q] == '>' and j[q] > j[q+1]: 
                re.append(j[q])
                re.append(j[q+1])
                back()
                re.pop()
            if sign[q] == '<' and j[q] < j[q+1]:
                re.append(j[q])
                re.append(j[q+1])
                back()
                re.pop()

    # print(*a, sep='')
```
