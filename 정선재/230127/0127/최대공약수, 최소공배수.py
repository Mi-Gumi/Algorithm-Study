a, b = map(int, input().split())
list_subin=list()
list_jeoghun = list()
list_gipyo = list()
for i in range(a):
    if a%(i+1) == 0 :
        list_subin.append(i+1)
for j in range(b):
    if b%(j+1) == 0:
        list_jeoghun.append(j+1)
for k in list_jeoghun:
    if k in list_subin:
        list_gipyo.append(k)
minwoo = max(list_gipyo)
seon = a*b//minwoo

print(minwoo)
print(seon)

