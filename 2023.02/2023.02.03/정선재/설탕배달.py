n = int(input())

i = 1
while i:
    if n % 5 == 0:
        print((n//5)+(i-1))
        break
    elif (n-(3*i))%5 == 0:
        print(i+((n-(3*i))//5))
        break
    elif 0< n-(3*i) < 3:
        print(-1)
        break 
    else :
        i += 1
   
    


