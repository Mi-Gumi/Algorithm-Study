n = int(input())
scores = []
for i in range(n):
    scores.append(int(input()))
sum_scores = []
if n == 1 :
    print(scores[0])
    
elif n == 2 :
    print(scores[0]+scores[1])
    
else:
    sum_scores.append(scores[0])
    sum_scores.append(scores[1]+scores[0])

    if scores[2]+scores[0] > scores[2]+scores[1]:
        sum_scores.append(scores[2]+scores[0])
    else :
        sum_scores.append(scores[2]+scores[1])
    
    for j in range(3,n):
        if scores[j]+sum_scores[j-2] > scores[j]+scores[j-1]+sum_scores[j-3]:
            sum_scores.append(scores[j]+sum_scores[j-2])
        else:
            sum_scores.append(scores[j]+scores[j-1]+sum_scores[j-3])

print(sum_scores[-1])