import sys
input = sys.stdin.readline
n = int(input())
top = list(map(int,input().split()))
ans = [0] * n
st = []
for i in range(len(top)):
    while st:
        if top[st[-1][0]] < top[i]:
            st.pop()
        else:
            ans[i] = st[-1][0]+1
            break
    st.append((i,top[i]))
print(*ans)
