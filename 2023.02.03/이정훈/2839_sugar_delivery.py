N = int(input())
count = 0
for i in range(N // 3 + 1):
    if N % 5 == 0:
        count += N // 5
        break
    else:
        N -= 3
        count += 1
else:
    count = -1
print(count)
