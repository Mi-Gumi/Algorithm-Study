x, y = map(int, input().split())

lst_x = list()
lst_y = list()
lst_x_y = list()

# x의 약수 저장
for i in range(1, x + 1):
    if not x % i:
        lst_x.append(i)

# y의 약수 저장
for i in range(1,y + 1):
    if not y % i:
        lst_y.append(i)

# 공통된 약수 저장
for num_x in lst_x:
    for num_y in lst_y:
        if num_x == num_y:
            lst_x_y.append(num_x)

# 최대공약수 출력
print(max(lst_x_y))
# 최소공배수는 x * y // 최대공약수
print(x * y // max(lst_x_y))

