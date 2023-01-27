import sys 
input = sys.stdin.readline
N = int(input())
arr_data = []
for _ in range(N) :
    arr_data.append(list(input().split()))
arr_data.sort(key=lambda x : int(x[0]))
for data in arr_data :
	print(f'{data[0]} {data[1]}')
	