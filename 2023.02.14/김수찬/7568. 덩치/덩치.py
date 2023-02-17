num = int(input())
people = []
    
for i in range(num):
    person = input()
    person = person.split()
    
    person[0] = int(person[0])
    person[1] = int(person[1])
    
    people.append(person)
ans = []

for i in range(len(people)):
    
    count = 0
    for j in range(len(people)):
        
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    ans.append(count+1)
    
for i in range(len(ans)):
    print(ans[i],end = ' ')
