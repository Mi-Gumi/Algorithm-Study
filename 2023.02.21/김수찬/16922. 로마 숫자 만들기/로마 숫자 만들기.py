num = [1,5,10,50]

N = int(input())

lst = list()
cnt = set()
def bt(n):
    global cnt
    if len(lst) == N:
        # print(lst)
        cnt.add(sum(lst))
        return

    for i in range(n,4):
        lst.append(num[i])
        bt(i)
        lst.pop()

for a in range(4):
    lst.append(num[a])
    bt(a)
    lst.pop()
print(len(cnt))
