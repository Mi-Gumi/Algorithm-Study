def rec(n,r,c,cnt) :
    mid = n//2
    m = mid*mid
    if n == 2 :
        return cnt + r*2+c
    if r < mid:
        if c < mid :
            ans  = rec(mid,r,c,cnt)
        else :
            ans  = rec(mid,r,c-mid,cnt+m)
    else :
        if c < mid :
            ans  = rec(mid,r-mid,c,cnt+2*m)
        else :
            ans  = rec(mid,r-mid,c-mid,cnt+3*m)
    
    return ans
N, r, c = map(int,input().split())

ans = rec(2**N,r,c,0)
print(ans)