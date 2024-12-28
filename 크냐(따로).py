while True:
    a,b=input().split()
    a=int(a)
    b=int(b)
    if a==0 and b==0:
        quit()
    else:
        if a>b:
            print('Yes')
        else:
            print('No')
