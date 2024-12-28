x=input().strip()

d=True
i=0

while i < len(x):
    if x[i]=='p':
        if i+1 < len(x) and x[i+1]=='i':
            i+=2

        else:
            d=False
            break
    elif x[i]=='k':
        if i+1 < len(x) and x[i+1]=='a':
            i+=2

        else:
            d=False
            break

    elif x[i]=='c':
        if i+2 < len(x) and x[i+1]=='h' and x[i+2]=='u':
            i+=3
        else:
            d=False
            break
    
    else:
        d=False
        break
if d:
    print('YES')
else:
    print('NO')

    


