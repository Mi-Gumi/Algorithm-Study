'''
가격이 싼 주유소에서 최대한 많이 필요한 만큼만
'''

n = int(input())
distance = list(map(int,input().split()))
oil = list(map(int,input().split()))

price = 10**9
total = 0
# 현재까지 나온 최저가 보다 싼 가격이 있으면 price 업데이트
for i in range(n-1) :
    if oil[i] < price :
        price = oil[i]
    total += distance[i] * price
print(total)