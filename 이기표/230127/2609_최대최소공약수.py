n1, n2 = map(int, input().split())

ans_yak = []
ans_bae = []

dict_yak = {}
dict_bae = {}

yak_li = []
bae_li = []

for i in range(1, n1+1):
    if n1 % i == 0: # 최소공약수
        ans_yak.append(i) # 약수를 리스트에 다 저장
    ans_bae.append(n2 * i) # 배수를 리스트에 다 저장

for j in range(1, n2+1):
    if n2 % j == 0: # 최소공약수
        ans_yak.append(j) # 약수를 리스트에 다 저장
    ans_bae.append(n1 * j) # 배수를 리스트에 다 저장

# 딕셔너리로 중복 확인
for yak in ans_yak: # 약수를 카운트해서 딕셔너리로 저장
    if yak not in dict_yak:
        dict_yak[yak] = 1
    else:
        dict_yak[yak] += 1

for bae in ans_bae: # 배수를 카운트해서 딕셔너리로 저장
    if bae not in dict_bae:
        dict_bae[bae] = 1
    else:
        dict_bae[bae] += 1
# 최소공약수, 최소공배수 확인
for k, v in dict_yak.items():
    if v == 2: # 공통되는 약수 찾기
        yak_li.append(k)

for k, v in dict_bae.items():
    if v == 2: # 공통되는 배수 찾기
        bae_li.append(k)

print(yak_li[-1]) # 최대공약수
print(bae_li[0]) # 최소공배수

