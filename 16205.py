a,b=input().split()
if a=='1':
    print(b)
    for i in list(b):
        if ord(i)<=96:
            i='_'+chr(ord(i)+32)
            print(i,end='')
        else:
            print(i,end='')
            
    cnt=0
    print()
    for i in list(b):
        if cnt==0:
            i=chr(ord(i)-32)
        cnt=1
        print(i,end='')
elif a=='2':
    k=list(b)
    for i in range(len(b)):
        if k[i]=='_':
            k[i]=''
            k[i+1]=chr(ord(k[i+1])-32)
        print(k[i],end='')
    print()
    print(b)
    cnt=0
    for i in k:
        if cnt==0:
            i=chr(ord(i)-32)
        cnt=1
        print(i,end='')
else:
    k=list(b)
    k[0]=chr(ord(k[0])+32)
    for i in k:
        print(i,end='')
    print()
    for i in k:
        if ord(i)<=96:
            i='_'+chr(ord(i)+32)
            print(i,end='')
        else:
            print(i,end='')
    print()
    print(b)



    
