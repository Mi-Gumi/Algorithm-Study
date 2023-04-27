formula = input()
# -로 나누고 합한 연산을 차례로 - 연산
split_minus = formula.split('-')

# print(split_minus)
arr = []
for plus in split_minus :
    arr.append(list(map(int,plus.split('+'))))
# print(arr)
ans = sum(arr[0])
for i in range(1, len(arr)) :
    ans -= sum(arr[i])
print(ans)