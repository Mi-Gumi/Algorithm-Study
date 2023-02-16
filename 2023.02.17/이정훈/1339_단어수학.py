N = int(input())

words = [input() for i in range(N)]
new_words = []

alpha_dict = {chr(65+i):0 for i in range(26)}
for word in words :
    for i in range(len(word)) :
        alpha_dict[word[-i-1]] += 10**i 

sorteddict = sorted(alpha_dict.items(),key=lambda x: x[1])

val_dict = {}  
for i in range(1,11):
    val_dict[sorteddict[-i][0]] = str(10-i)

for i in range(N) :
    newword = ''
    for c in words[i]:
        newword += val_dict[c]
    new_words.append(int(newword))
    
ans = sum(new_words)
print(ans)
    