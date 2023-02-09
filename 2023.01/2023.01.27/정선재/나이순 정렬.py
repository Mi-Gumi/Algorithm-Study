N = int(input())
c = list()
for i in range(N):
    name = input()
    a, b = name.split()
    c.append([b, int(a)]) 

c.sort(key = lambda x : x[1])
for j in c:
    print(j[1],j[0])


