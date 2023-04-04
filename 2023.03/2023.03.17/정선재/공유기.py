N,C = map(int,input().split())
H = []
for _ in range(N):
    n = int(input())
    H.append(n)

H.sort()

def find(H,start,end):
    while start <= end:
        mid =(start+end)//2
        current = H[0]
        cnt = 1

        for i in range(1,len(H)):
            if H[i] >= current + mid:
                cnt += 1
                current = H[i]
        
        if cnt >= C:
            global ans
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

start = 1
end = H[-1] - H[0]
ans = 0

find(H, start, end)
print(ans)