#이정훈
import sys 
input = sys.stdin.readline
N = int(input())
coordinates = []
for i in range(N) :
    input_xy = list(map(int,input().split()))
    coordinates.append(input_xy)
coordinates.sort(key = lambda x : x[1])
coordinates.sort(key = lambda x : x[0])
for i in coordinates :
	print(f'{i[0]} {i[1]}')