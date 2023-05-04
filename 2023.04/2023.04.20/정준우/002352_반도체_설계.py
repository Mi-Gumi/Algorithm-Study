from sys import stdin
from bisect import bisect_left


# 이전 과정에서 연결된 우측 포트보다 더 위의 포트에 연결되면 꼬이는 것
# 가장 긴 증가하는 부분 수열의 길이를 구하면 연결할 수 있는 포트의 최대 수를 구할 수 있음
num_of_ports = int(stdin.readline())

connections = list(map(int, stdin.readline().split()))

connected_ports = []

for connection in connections:

    if not connected_ports or connected_ports[-1] < connection:
        connected_ports.append(connection)

    else:
        connected_ports[bisect_left(connected_ports, connection)] = connection

print(len(connected_ports))
