import sys
input = sys.stdin.readline

N = int(input())

# 나이와 이름을 담을 배열 선언
clients = list()

# 나이는 정수형으로 이름은 문자열으로 묶은 리스트를 clients에 추가
for _ in range(N):
    age, name = input().split()
    age = int(age)
    clients.append([age, name])

# 리스트의 0번을 키로 clients 정렬
clients.sort(key=lambda x: x[0])

for d in clients:
    print(d[0], d[1])
