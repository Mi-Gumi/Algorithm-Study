T = int(input())

cols = [list(map(int,input().split())) for _ in range(T)]
cols.sort(key= lambda x: x[0])

x = cols[0][0]
y = cols[0][1]
result = 0
top = max(cols,key=lambda x: x[1])
ti = cols.index(top)

for i in range(ti+1): 
    X, Y = cols[i]
    if Y >= y:
        result += (X-x)*(y)
        x = X
        y = Y
result += top[1]

x = cols[len(cols)-1][0]
y = cols[len(cols)-1][1]
for i in range(len(cols)-1,ti-1,-1):
    X, Y = cols[i]
    if Y >= y:
        result += (x-X)*(y)
        x = X
        y = Y

print(result)