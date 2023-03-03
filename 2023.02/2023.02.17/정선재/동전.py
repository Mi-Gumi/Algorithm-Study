import sys
input = sys.stdin.readline

N, target = map(int,input().split())
coin_list = []
for i in range(N):
    coin = int(input())
    if coin <= target:
        coin_list.append(coin)
coin_list.sort(reverse=True)
count = 0

for i in range(len(coin_list)):
    if target % coin_list[i]== 0 :
        count += target//coin_list[i]
        break
    else:
        count += target//coin_list[i]
        target = target % coin_list[i]

print(count)