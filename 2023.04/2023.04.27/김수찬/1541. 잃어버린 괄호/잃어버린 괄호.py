texts = input()
texts_ = texts.split('-')
# print(texts)

ans = 0
x = sum(map(int, (texts_[0].split('+'))))
if texts[0] == '-':
    ans -= x
else:
    ans += x

for x in texts_[1:]:
    x = sum(map(int, (x.split('+'))))
    ans -= x
print(ans)