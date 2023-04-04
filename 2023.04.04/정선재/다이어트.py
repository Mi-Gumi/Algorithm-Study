from sys import stdin
from itertools import combinations

n = int(input())
mp,mf,ms,mv = map(int,input().split())

board = [[]]
for _ in range(n):
    p,f,s,v,c = map(int,input().split())
    board.append((p,f,s,v,c))


def solv():
    price = 10**9
    ans = None
    for i in range(1,n+1):
        for comb in combinations(range(1,n+1),i):
            tp=tf=ts=tv=tc=0
            for j in comb:
                tp += board[j][0]
                tf += board[j][1]
                ts += board[j][2]
                tv += board[j][3]
                tc += board[j][4]
            
            if tp >=mp and tf >= mf and ts>= ms and tv >= mv:
                if price > tc:
                    price = tc
                    ans = comb
                elif price == tc:
                    ans = sorted((ans,comb))[0]
    
    if price == 10**9:
        print(-1)
    else:
        print(price)
        print(*ans)

solv()