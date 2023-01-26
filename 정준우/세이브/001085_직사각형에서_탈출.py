x, y, w, h = map(int, input().split())

distance_list = list()

# x 좌표에서 짧은 방향 찾기
if x <= (w - x):
    distance_list.append(x)
else:
    distance_list.append(w - x)

# y 좌표에서 짧은 방향 찾기
if y <= (h - y):
    distance_list.append(y)
else:
    distance_list.append(h - y)

# x, y 좌표 중 더 짧은 방향 찾기
print(min(distance_list))