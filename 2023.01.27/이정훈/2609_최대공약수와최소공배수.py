#이정훈
N , M = map(int,input().split())
max_divisor = 1
min_multiple = N*M
for i in range(1,max(N,M)+1) :
	if N % i == 0 and M % i == 0 and i > max_divisor :
		max_divisor = i
for i in range(min(N,M),N*M+1,min(N,M)) :
	if i % N == 0 and i % M == 0 :
		min_multiple = i 
		break
print(max_divisor)
print(min_multiple)
	