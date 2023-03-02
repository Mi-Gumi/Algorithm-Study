N = int(input())

words = [input() for i in range(N)]
new_words = []            # 숫자로 변환된 단어를 저장할 리스트

alpha_dict = {chr(65+i):0 for i in range(26)}        # {'A':0,'B':0,....}  가중치값이 저장될 dict
for word in words :
    for i in range(len(word)) :
        alpha_dict[word[-i-1]] += 10**i              
        
        # 가장 높은 자리수에 많은 알파벳부터 9를 부여하는 것이 최선이므로
        # 카운트할 때 각 자리수를 더해줌
        # 단어의 오른쪽끝이 1의 자리이므로 10의 0승 이후부터 10의 1승....

sorteddict = sorted(alpha_dict.items(),key=lambda x: x[1]) # 사전의 키와 벨류 중 벨류를 기준으로 오름차순 정렬



val_dict = {}   # ex) 'A' : 9 같은 정보를 저장할 사전
for i in range(1,11):
    val_dict[sorteddict[-i][0]] = str(10-i)    # 오름차순으로 정렬된 아이템의 키값을 키로 넣어주고 9부터 순서대로 저장

for i in range(N) :
    newword = ''         # 바뀐 단어가 저장될 문자열
    for c in words[i]:
        newword += val_dict[c]      # 알파벳에 해당하는 숫자가 끝에 붙여짐
    new_words.append(int(newword))  # int로 변환한 뒤 리스트에 추가
    
ans = sum(new_words)   # sum
print(ans)
    