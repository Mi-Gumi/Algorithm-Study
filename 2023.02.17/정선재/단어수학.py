val = [9,8,7,6,5,4,3,2,1,0]
N = int(input())
arr = []
for i in range(N):
    a = list(map(str,input()))
    b = [len(a), a]
    arr.append(b)
arr.sort(reverse=True)
arr2 = []
for i in range(len(arr)):
    arr2.append(arr[i][1]) 

for i in range(val